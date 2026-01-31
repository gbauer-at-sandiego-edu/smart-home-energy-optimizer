# src/data_ingest.py
"""
Loads UK-DALE from ukdale.h5 (HDF5) and prepares a manageable 1-minute dataset slice.

Key design choices:
- Read data from Kaggle mirror HDF5 (ukdale.h5)
- Use Building 1
- Use memory-safe slicing (no PyTables time-string where clauses)
- Resample to 1-minute
- Output a small processed CSV (do NOT commit the big raw dataset to GitHub)
"""

from pathlib import Path
from glob import glob
import pandas as pd

from src.config import (
    MAINS_KEY,
    KETTLE_KEY,
    RESAMPLE_RULE,
    DAYS_TO_USE,
    KETTLE_ON_THRESHOLD_W,
)


def find_h5(data_dir: Path) -> Path:
    cands = (
        glob(str(data_dir / "**" / "*.h5"), recursive=True)
        + glob(str(data_dir / "**" / "*.hdf5"), recursive=True)
    )
    if not cands:
        raise FileNotFoundError("No .h5/.hdf5 found under dataset directory.")
    return Path(cands[0])


def load_meter_slice_1m_no_where(
    h5_path: Path,
    key: str,
    days: int,
    start_time=None,
    resample_rule: str = "1min",
    stop_rows: int = 5_000_000,
):
    """
    Avoid PyTables date parsing issues by NOT using:
        where=[f"index>=...", f"index<=..."]
    Instead, we load rows then filter timestamps in pandas.
    """
    with pd.HDFStore(h5_path, mode="r") as store:
        head = store.select(key, start=0, stop=50_000)
        if head.empty:
            raise RuntimeError(f"Empty head for key {key}")

        head.index = pd.to_datetime(head.index, errors="coerce")
        t0 = head.index.min() if start_time is None else pd.to_datetime(start_time)
        t1 = t0 + pd.Timedelta(days=days)

        df = store.select(key, start=0, stop=stop_rows)

    df.index = pd.to_datetime(df.index, errors="coerce")
    df = df.loc[(df.index >= t0) & (df.index <= t1)]

    if df.empty:
        raise RuntimeError("No rows in requested time window. Increase stop_rows.")

    s = df.iloc[:, 0]
    s1m = s.resample(resample_rule).mean().dropna()
    return s1m, t0, t1


def build_df_1m(h5_path: Path) -> pd.DataFrame:
    mains_1m, t0, t1 = load_meter_slice_1m_no_where(
        h5_path, MAINS_KEY, DAYS_TO_USE, resample_rule=RESAMPLE_RULE
    )
    kettle_1m, _, _ = load_meter_slice_1m_no_where(
        h5_path, KETTLE_KEY, DAYS_TO_USE, start_time=t0, resample_rule=RESAMPLE_RULE
    )

    df_1m = pd.DataFrame({"mains_W": mains_1m, "kettle_W": kettle_1m}).dropna()

    # quick label check (helps us confirm the kettle meter really has ON events)
    df_1m["kettle_on"] = (df_1m["kettle_W"] >= KETTLE_ON_THRESHOLD_W).astype(int)

    return df_1m


def save_processed_csv(df_1m: pd.DataFrame, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_1m.to_csv(out_path, index=True)


if __name__ == "__main__":
    # Run this in Colab or locally (with deps installed).
    # Example flow:
    #   python -m src.data_ingest
    import kagglehub

    data_dir = Path(kagglehub.dataset_download("abdelmdz/uk-dale"))
    h5_path = find_h5(data_dir)
    print("H5 path:", h5_path)

    df_1m = build_df_1m(h5_path)

    print("Rows:", len(df_1m))
    print(df_1m[["mains_W", "kettle_W", "kettle_on"]].head())

    print("kettle_on counts:")
    print(df_1m["kettle_on"].value_counts(dropna=False))

    out_csv = Path("data/processed/building1_mains_kettle_1min_180d.csv")
    save_processed_csv(df_1m, out_csv)
    print("Wrote:", out_csv)

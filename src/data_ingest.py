# src/data_ingest.py
#
# Multi-house ingestion for UK-DALE.
# Extracts mains + kettle channels for any house, resamples to 1-minute,
# and returns a clean dataframe ready for downstream NILM tasks.

from pathlib import Path
import pandas as pd
import h5py


def extract_house_channels(h5_path: Path, house: int):
    """
    Extracts mains + kettle channels + timestamps for a given house.

    Expected UK-DALE structure:
        /house_1/mains
        /house_1/kettle
        /house_1/timestamps

    Returns:
        pd.DataFrame with columns:
            - index (datetime)
            - power_watts
            - kettle_watts
    """

    with h5py.File(h5_path, "r") as f:
        group_name = f"house_{house}"
        if group_name not in f:
            raise ValueError(f"House {house} not found in HDF5 file.")

        grp = f[group_name]

        mains = grp["mains"][:]          # watts
        kettle = grp["kettle"][:]        # watts
        timestamps = grp["timestamps"][:]  # unix timestamps

    df = pd.DataFrame({
        "index": pd.to_datetime(timestamps, unit="s", utc=True),
        "power_watts": mains,
        "kettle_watts": kettle,
    })

    df = df.set_index("index").sort_index()
    return df


def build_df_1m(h5_path: Path, house: int):
    """
    Extracts raw data for a house and resamples to 1-minute resolution.

    Resampling + interpolation:
        - Smooths missing timestamps
        - Produces consistent intervals for CNN/LSTM models
    """

    df_raw = extract_house_channels(h5_path, house)

    df_1m = (
        df_raw
        .resample("1T")
        .mean()
        .interpolate()
    )

    return df_1m


def save_processed_csv(df: pd.DataFrame, out_path: Path):
    """
    Saves a processed dataframe to CSV.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=True)
    print("Saved:", out_path)

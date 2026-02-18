"""
Pipeline orchestrator for the Smart Home Energy Optimizer.

This version removes all ingestion logic and operates entirely
on pre-cleaned CSVs:
- House_1_kettle_analysis.csv  (CNN test)
- House_2_kettle_analysis.csv  (CNN train)
- House_1_cleaned.csv          (LSTM forecasting)

The pipeline supports:
    full        → CNN + LSTM
    cnn_only    → CNN NILM only
    lstm_only   → LSTM forecasting only
"""

import argparse
from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
SRC_DIR = THIS_FILE.parent
PROJECT_ROOT = SRC_DIR.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models.cnn_nilm import train_cnn_nilm
from src.models.lstm_forecast import train_lstm_forecaster


# ------------------------------------------------------------
# Directory setup
# ------------------------------------------------------------
def ensure_dirs():
    (SRC_DIR / "models").mkdir(parents=True, exist_ok=True)
    (SRC_DIR / "data" / "processed").mkdir(parents=True, exist_ok=True)
    (SRC_DIR / "data" / "reports").mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Main entry point
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="CSV-based Smart Home Energy Optimizer Pipeline")

    parser.add_argument(
        "--mode",
        type=str,
        default="full",
        choices=["full", "cnn_only", "lstm_only"],
        help="Which stages to run.",
    )

    # CNN NILM inputs
    parser.add_argument(
        "--house1_csv",
        type=str,
        default=str(SRC_DIR / "data" / "interim" / "House_1_kettle_analysis.csv"),
        help="House 1 mains + kettle CSV.",
    )

    parser.add_argument(
        "--house2_csv",
        type=str,
        default=str(SRC_DIR / "data" / "interim" / "House_2_kettle_analysis.csv"),
        help="House 2 mains + kettle CSV.",
    )

    # LSTM input
    parser.add_argument(
        "--house1_cleaned_csv",
        type=str,
        default=str(SRC_DIR / "data" / "interim" / "House_1_cleaned.csv"),
        help="House 1 cleaned aggregate CSV.",
    )

    args = parser.parse_args()
    ensure_dirs()

    models_dir = SRC_DIR / "models"
    reports_dir = SRC_DIR / "data" / "reports"

    # -----------------------------
    # CNN NILM
    # -----------------------------
    if args.mode in ("full", "cnn_only"):
        train_cnn_nilm(
            house2_csv=Path(args.house2_csv),
            house1_csv=Path(args.house1_csv),
            output_models_dir=models_dir,
            output_reports_dir=reports_dir,
        )

    # -----------------------------
    # LSTM forecasting
    # -----------------------------
    if args.mode in ("full", "lstm_only"):
        train_lstm_forecaster(
            house1_cleaned_csv=Path(args.house1_cleaned_csv),
            output_models_dir=models_dir,
            output_reports_dir=reports_dir,
        )


if __name__ == "__main__":
    main()

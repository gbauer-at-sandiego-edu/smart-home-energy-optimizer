# src/data_download.py
"""
Downloads the UK-DALE dataset (Kaggle mirror) into the current runtime using kagglehub.
This avoids Google Drive mounting and avoids the unreliable UKERC zip.
"""

from pathlib import Path
import kagglehub


def download_ukdale() -> Path:
    data_dir = kagglehub.dataset_download("abdelmdz/uk-dale")
    return Path(data_dir)


if __name__ == "__main__":
    p = download_ukdale()
    print("Downloaded UK-DALE to:", p)

"""
LSTM-based forecasting model for aggregate mains power.

This module implements the *original* hourly LSTM forecaster used
before the project migrated to minute-level sampling.

Design characteristics of this legacy model:
- Uses a 168-hour (1-week) lookback window.
- Predicts the next hour of aggregate mains power.
- Resamples using "1h" (the modern pandas alias for hourly data).
- Uses tf.keras.Input to avoid deprecated input_shape warnings.
- Saves models in `.keras` format for forward compatibility.

This file is preserved for documentation and comparison purposes.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras import layers, models


# ------------------------------------------------------------
# Data loading
# ------------------------------------------------------------
def _load_series(csv_path: Path):
    """
    Load a cleaned aggregate CSV containing:
        index, power_watts

    Responsibilities:
    - Validate required columns
    - Parse timestamps
    - Sort chronologically
    - Return a clean DataFrame ready for resampling
    """
    df = pd.read_csv(csv_path)

    # Ensure required fields exist and contain no missing values
    df.dropna(subset=["index", "power_watts"], inplace=True)

    # Convert index column to timezone-aware datetime
    df["index"] = pd.to_datetime(df["index"], utc=True)

    # Ensure chronological ordering
    df.sort_values("index", inplace=True)

    return df


# ------------------------------------------------------------
# Windowing utility
# ------------------------------------------------------------
def _create_windows(series: np.ndarray, window: int):
    """
    Convert a univariate time series into supervised learning windows.

    For each position i:
        X[i] = series[i : i+window]
        y[i] = series[i+window]

    This produces:
        X: (num_samples, window, 1)
        y: (num_samples,)

    This framing supports sequence-to-one forecasting.
    """
    X, y = [], []
    for i in range(len(series) - window):
        X.append(series[i:i+window])
        y.append(series[i+window])
    return np.array(X), np.array(y)


# ------------------------------------------------------------
# Model definition
# ------------------------------------------------------------
def _build_lstm(input_length: int) -> tf.keras.Model:
    """
    Construct a two-layer LSTM forecaster.

    Architecture rationale:
    - First LSTM layer returns sequences to allow stacked temporal learning.
    - Second LSTM layer compresses sequence into a latent representation.
    - Dense(1) outputs the next-hour prediction.

    Uses tf.keras.Input to avoid legacy warnings.
    """
    return models.Sequential([
        tf.keras.Input(shape=(input_length, 1)),
        layers.LSTM(64, return_sequences=True),
        layers.LSTM(32),
        layers.Dense(1),
    ])


# ------------------------------------------------------------
# Training entry point
# ------------------------------------------------------------
def train_lstm_forecaster(
    house1_cleaned_csv: Path,
    output_models_dir: Path,
    output_reports_dir: Path,
    window: int = 168,   # 168 hours = 1 week lookback
):
    """
    Train the legacy hourly LSTM forecaster on House 1 aggregate mains.

    Workflow:
        1. Load cleaned CSV
        2. Resample to hourly resolution ("1h")
        3. Scale using MinMaxScaler
        4. Create sliding windows
        5. Train LSTM with early stopping
        6. Save model + scaler

    Outputs:
        - lstm_house1_forecast.keras
        - lstm_scaler_house1.pkl
    """
    # Ensure output directories exist
    output_models_dir.mkdir(parents=True, exist_ok=True)
    output_reports_dir.mkdir(parents=True, exist_ok=True)

    # -----------------------------
    # Load and resample data
    # -----------------------------
    df = _load_series(house1_cleaned_csv)

    # Use "1h" instead of deprecated "H"
    df_resampled = df.resample("1h", on="index").mean().interpolate()

    # Extract univariate series
    series = df_resampled["power_watts"].values.reshape(-1, 1)

    # -----------------------------
    # Scaling
    # -----------------------------
    scaler = MinMaxScaler()
    series_scaled = scaler.fit_transform(series)

    # -----------------------------
    # Windowing
    # -----------------------------
    X, y = _create_windows(series_scaled, window)

    # Reshape for LSTM: (samples, timesteps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Train/test split (80/20)
    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    print(f"Training shape: {X_train.shape}")
    print(f"Testing shape: {X_test.shape}")

    # -----------------------------
    # Build & train model
    # -----------------------------
    model = _build_lstm(window)
    model.compile(optimizer="adam", loss="mse")

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True,
        )
    ]

    model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=50,
        batch_size=32,
        callbacks=callbacks,
        verbose=1,
    )

    # -----------------------------
    # Save model + scaler
    # -----------------------------
    model_path = output_models_dir / "lstm_house1_forecast.keras"
    model.save(model_path)

    import joblib
    scaler_path = output_models_dir / "lstm_scaler_house1.pkl"
    joblib.dump(scaler, scaler_path)

    print(f"LSTM model saved to: {model_path}")
    print(f"Scaler saved to: {scaler_path}")

"""
LSTM-based forecasting model for aggregate mains power.

This module trains a sequence-to-one LSTM forecaster on the
cleaned House 1 aggregate series. The design uses a 168-hour
(1-week) lookback window and predicts the next hour. All warnings
are eliminated by:
- Using tf.keras.Input instead of input_shape
- Using "1h" instead of deprecated "H" for resampling
- Saving models in `.keras` format
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
    Load a cleaned aggregate CSV with:
        index, power_watts
    """
    df = pd.read_csv(csv_path)
    df.dropna(subset=["index", "power_watts"], inplace=True)

    df["index"] = pd.to_datetime(df["index"], utc=True)
    df.sort_values("index", inplace=True)

    return df


# ------------------------------------------------------------
# Windowing utility
# ------------------------------------------------------------
def _create_windows(series: np.ndarray, window: int):
    """
    Convert a univariate series into (X,y) windows for forecasting.
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
    Two-layer LSTM forecaster with modern Keras Input API.
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
    window: int = 168,
):
    """
    Train an LSTM forecaster on House 1 aggregate mains.
    Saves:
        - lstm_house1_forecast.keras
        - lstm_scaler_house1.pkl
    """
    output_models_dir.mkdir(parents=True, exist_ok=True)
    output_reports_dir.mkdir(parents=True, exist_ok=True)

    df = _load_series(house1_cleaned_csv)

    # Fix pandas warning: use "1h" instead of "H"
    df_resampled = df.resample("1h", on="index").mean().interpolate()

    series = df_resampled["power_watts"].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    series_scaled = scaler.fit_transform(series)

    X, y = _create_windows(series_scaled, window)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    print(f"Training shape: {X_train.shape}")
    print(f"Testing shape: {X_test.shape}")

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

    model_path = output_models_dir / "lstm_house1_forecast.keras"
    model.save(model_path)

    import joblib
    scaler_path = output_models_dir / "lstm_scaler_house1.pkl"
    joblib.dump(scaler, scaler_path)

    print(f"LSTM model saved to: {model_path}")
    print(f"Scaler saved to: {scaler_path}")

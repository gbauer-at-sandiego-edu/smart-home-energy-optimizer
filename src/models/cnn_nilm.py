"""
CNN-based NILM classifier for kettle detection.

This module trains a convolutional classifier on House 2
(mains + kettle_watts) and evaluates on House 1. The design
assumes a binary classification target derived from kettle_watts
via a threshold. The model architecture uses modern Keras APIs
(tf.keras.Input) to avoid legacy warnings and ensure forward
compatibility.

Key engineering decisions:
- Window-based framing converts a univariate time series into
  short sequences suitable for 1D CNN feature extraction.
- Binary label is computed as max(kettle_watts > threshold)
  within each window, capturing short-duration activations.
- MinMaxScaler ensures stable gradient behavior.
- Model saved in `.keras` format (recommended by Keras).
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras import layers, models


# ------------------------------------------------------------
# Data loading and preprocessing
# ------------------------------------------------------------
def _load_labeled_series(csv_path: Path, kettle_threshold: float = 10.0):
    """
    Load a labeled NILM CSV containing:
        index, power_watts, kettle_watts

    Returns:
        mains: (N,1) float array
        labels: (N,) binary array
        timestamps: datetime array
    """
    df = pd.read_csv(csv_path)

    required = ["index", "power_watts", "kettle_watts"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns in {csv_path}: {missing}")

    df.dropna(subset=required, inplace=True)
    df["index"] = pd.to_datetime(df["index"], utc=True)
    df.sort_values("index", inplace=True)

    mains = df["power_watts"].values.reshape(-1, 1)
    labels = (df["kettle_watts"].values >= kettle_threshold).astype(int)

    return mains, labels, df["index"].values


# ------------------------------------------------------------
# Model definition
# ------------------------------------------------------------
def _build_cnn(input_length: int) -> tf.keras.Model:
    """
    Construct a compact 1D CNN for binary NILM classification.
    Uses tf.keras.Input to avoid deprecated input_shape warnings.
    """
    return models.Sequential([
        tf.keras.Input(shape=(input_length, 1)),
        layers.Conv1D(32, kernel_size=3, activation="relu", padding="same"),
        layers.MaxPooling1D(pool_size=2),
        layers.Conv1D(64, kernel_size=3, activation="relu", padding="same"),
        layers.MaxPooling1D(pool_size=2),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ])


# ------------------------------------------------------------
# Windowing utility
# ------------------------------------------------------------
def _create_windows(series: np.ndarray, labels: np.ndarray, window: int):
    """
    Convert a univariate series + labels into sliding windows.

    Label for each window = max(label in window), capturing
    any kettle activation within the window.
    """
    X, y = [], []
    for i in range(len(series) - window + 1):
        X.append(series[i:i+window])
        y.append(int(labels[i:i+window].max()))
    return np.array(X), np.array(y)


# ------------------------------------------------------------
# Training entry point
# ------------------------------------------------------------
def train_cnn_nilm(
    house2_csv: Path,
    house1_csv: Path,
    output_models_dir: Path,
    output_reports_dir: Path,
    window: int = 24,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Train CNN NILM on House 2 and evaluate on House 1.
    Saves:
        - cnn_kettle_house2.keras
        - cnn_kettle_scaler_house2.pkl
        - cnn_kettle_house1_eval.txt
    """
    output_models_dir.mkdir(parents=True, exist_ok=True)
    output_reports_dir.mkdir(parents=True, exist_ok=True)

    # -----------------------------
    # Load House 2 (training)
    # -----------------------------
    mains2, labels2, _ = _load_labeled_series(house2_csv)

    scaler = MinMaxScaler()
    mains2_scaled = scaler.fit_transform(mains2)

    X2, y2 = _create_windows(mains2_scaled, labels2, window)
    X2 = X2.reshape((X2.shape[0], X2.shape[1], 1))

    X_train, X_val, y_train, y_val = train_test_split(
        X2, y2, test_size=test_size, random_state=random_state, stratify=y2
    )

    # -----------------------------
    # Build & train CNN
    # -----------------------------
    model = _build_cnn(window)
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

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
        validation_data=(X_val, y_val),
        epochs=50,
        batch_size=32,
        callbacks=callbacks,
        verbose=1,
    )

    # Save model in modern format
    model_path = output_models_dir / "cnn_kettle_house2.keras"
    model.save(model_path)

    # Save scaler
    import joblib
    scaler_path = output_models_dir / "cnn_kettle_scaler_house2.pkl"
    joblib.dump(scaler, scaler_path)

    # -----------------------------
    # Evaluate on House 1
    # -----------------------------
    mains1, labels1, _ = _load_labeled_series(house1_csv)
    mains1_scaled = scaler.transform(mains1)

    X1, y1 = _create_windows(mains1_scaled, labels1, window)
    X1 = X1.reshape((X1.shape[0], X1.shape[1], 1))

    eval_results = model.evaluate(X1, y1, verbose=0)

    report_path = output_reports_dir / "cnn_kettle_house1_eval.txt"
    with report_path.open("w") as f:
        f.write(f"loss: {eval_results[0]:.4f}, accuracy: {eval_results[1]:.4f}\n")

    print(f"CNN NILM model saved to: {model_path}")
    print(f"Scaler saved to: {scaler_path}")
    print(f"House 1 evaluation report: {report_path}")

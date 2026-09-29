from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

import joblib
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("ml_regression_inference")

# Define Paths
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "regression_model.joblib"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"

# Default values if user presses Enter without typing anything
DEFAULT_INPUTS: dict[str, str] = {
    "VendorID": "1",
    "passenger_count": "1",
    "trip_distance": "2.5",
    "RatecodeID": "1",
    "PULocationID": "142",
    "DOLocationID": "236",
    "payment_type": "1",
    "fare_amount": "12.50",
    "mta_tax": "0.50",
    "tolls_amount": "0.00",
    "improvement_surcharge": "0.30",
}


def load_artifacts() -> tuple[Any, list[str]]:
    """Load the trained scikit-learn pipeline and expected feature list."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    if not METADATA_PATH.exists():
        raise FileNotFoundError(f"Metadata file not found at {METADATA_PATH}")

    model = joblib.load(MODEL_PATH)

    with METADATA_PATH.open("r", encoding="utf-8") as file:
        metadata = json.load(file)

    numeric_features = metadata["features"]["numeric"]
    logger.info("Loaded model from %s", MODEL_PATH)
    return model, numeric_features


def parse_numeric_value(raw_val: str) -> float:
    """Clean string (remove $, commas, spaces) and parse to float."""
    cleaned = raw_val.strip().replace(",", "").lstrip("$")
    return float(cleaned)


def collect_user_inputs(expected_features: list[str]) -> dict[str, float]:
    """Interactively ask user for each numerical feature via console input."""
    print("\n" + "=" * 50)
    print(" TAXI TIP PREDICTOR - INPUT FEATURE VALUES")
    print(" (Press ENTER to use the default value)")
    print("=" * 50 + "\n")

    user_data: dict[str, float] = {}

    for feature in expected_features:
        default_val = DEFAULT_INPUTS.get(feature, "0.0")

        while True:
            raw_input = input(f"Enter {feature} [default: {default_val}]: ").strip()

            # If user presses Enter, use default value
            if not raw_input:
                raw_input = default_val

            try:
                numeric_val = parse_numeric_value(raw_input)
                user_data[feature] = numeric_val
                break
            except ValueError:
                print(
                    f"❌ Invalid input: '{raw_input}'. Please enter a valid number (e.g., 2.5 or 12).\n"
                )

    return user_data


def predict_from_dict(
    input_data: dict[str, float],
    model: Any,
    expected_features: list[str],
) -> float:
    """Predict tip amount for sanitized user input data."""
    df_input = pd.DataFrame([input_data])[expected_features]
    prediction = model.predict(df_input)[0]
    return float(prediction)


def main() -> None:
    # 1. Load artifacts
    model, expected_features = load_artifacts()

    # 2. Interactively collect values from the terminal
    user_inputs = collect_user_inputs(expected_features)

    # 3. Perform Prediction
    predicted_tip = predict_from_dict(user_inputs, model, expected_features)

    # 4. Display Result
    print("\n" + "=" * 50)
    print(" INFERENCE RESULT")
    print("=" * 50)
    print(f"Predicted Tip Amount: ${predicted_tip:.2f}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
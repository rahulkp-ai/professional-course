from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("taxi_tip_api")

# Define Paths
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "regression_model.joblib"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"
INDEX_HTML_PATH = BASE_DIR / "index.html"

# Global state for loaded model and metadata
model_pipeline: Any = None
model_metadata: Dict[str, Any] = {}


def load_model_artifacts() -> None:
    """Load model pipeline and metadata into memory."""
    global model_pipeline, model_metadata

    if not MODEL_PATH.exists():
        logger.error(f"Model file missing at: {MODEL_PATH}")
        raise FileNotFoundError(f"Model binary not found at {MODEL_PATH}")
    if not METADATA_PATH.exists():
        logger.error(f"Metadata file missing at: {METADATA_PATH}")
        raise FileNotFoundError(f"Metadata file not found at {METADATA_PATH}")

    model_pipeline = joblib.load(MODEL_PATH)
    with METADATA_PATH.open("r", encoding="utf-8") as f:
        model_metadata = json.load(f)

    logger.info("Successfully loaded model and metadata artifacts")


# Initialize FastAPI App
app = FastAPI(
    title="NYC Taxi Tip Prediction API",
    description="Machine Learning API powered by a Decision Tree Regressor.",
    version="1.0.0",
)

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event() -> None:
    """Run model artifact loader when FastAPI starts."""
    try:
        load_model_artifacts()
    except Exception as exc:
        logger.critical(f"Failed to load artifacts on startup: {exc}")


class TaxiTripInput(BaseModel):
    VendorID: float = Field(default=1.0, description="TLC vendor ID")
    passenger_count: float = Field(default=1.0, ge=0, description="Number of passengers")
    trip_distance: float = Field(default=2.5, ge=0.0, description="Trip distance in miles")
    RatecodeID: float = Field(default=1.0, description="Rate code ID")
    PULocationID: float = Field(default=142.0, description="TLC Taxi Zone Pickup Location ID")
    DOLocationID: float = Field(default=236.0, description="TLC Taxi Zone Dropoff Location ID")
    payment_type: float = Field(default=1.0, description="Payment type code (1=Credit Card, 2=Cash)")
    fare_amount: float = Field(default=12.50, ge=0.0, description="Base fare amount")
    mta_tax: float = Field(default=0.50, ge=0.0, description="MTA tax surcharge")
    tolls_amount: float = Field(default=0.00, ge=0.0, description="Tolls paid")
    improvement_surcharge: float = Field(default=0.30, ge=0.0, description="Improvement surcharge")


class PredictionOutput(BaseModel):
    predicted_tip: float
    total_estimated_cost: float
    tip_percentage: float


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def serve_dashboard():
    """Serve index.html at root endpoint."""
    if INDEX_HTML_PATH.exists():
        return INDEX_HTML_PATH.read_text(encoding="utf-8")
    return "<h1>Taxi Tip Predictor API</h1><p>API active. Visit <a href='/docs'>/docs</a> for docs.</p>"


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint to verify service and model status."""
    return {
        "status": "healthy" if model_pipeline is not None else "degraded",
        "model_loaded": model_pipeline is not None,
        "artifacts_directory": str(ARTIFACTS_DIR),
    }


@app.get("/metadata")
def get_metadata():
    """Return model training metadata and metrics."""
    if not model_metadata:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model metadata is not loaded.",
        )
    return model_metadata


@app.post("/predict", response_model=PredictionOutput)
def predict_tip(payload: TaxiTripInput):
    """Predict expected tip amount from input trip features."""
    if model_pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model pipeline not loaded properly.",
        )

    try:
        input_data = payload.model_dump()
        expected_features = model_metadata.get("features", {}).get(
            "numeric", list(input_data.keys())
        )

        df_input = pd.DataFrame([input_data])[expected_features]
        raw_prediction = model_pipeline.predict(df_input)[0]
        predicted_tip = max(0.0, round(float(raw_prediction), 2))

        base_fare = payload.fare_amount
        total_cost = round(
            base_fare
            + payload.mta_tax
            + payload.tolls_amount
            + payload.improvement_surcharge
            + predicted_tip,
            2,
        )
        tip_pct = round((predicted_tip / base_fare * 100) if base_fare > 0 else 0.0, 1)

        return PredictionOutput(
            predicted_tip=predicted_tip,
            total_estimated_cost=total_cost,
            tip_percentage=tip_pct,
        )

    except Exception as exc:
        logger.error(f"Inference error: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference failed: {str(exc)}",
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
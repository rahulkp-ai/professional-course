from __future__ import annotations

import json
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# ============================================================
# LOGGING SETUP
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("fraud_detection_api")

# ============================================================
# PATHS & GLOBAL ARTIFACT CONTAINER
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "svm_model.joblib"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"

artifacts: dict[str, Any] = {}


# ============================================================
# APPLICATION LIFESPAN (Load model on startup)
# ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load ML model pipeline and metadata into memory at API startup."""
    logger.info("Initializing API and loading model artifacts...")
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file missing at {MODEL_PATH}")
    if not METADATA_PATH.exists():
        raise FileNotFoundError(f"Metadata file missing at {METADATA_PATH}")

    model = joblib.load(MODEL_PATH)
    with METADATA_PATH.open("r", encoding="utf-8") as f:
        metadata = json.load(f)

    artifacts["model"] = model
    artifacts["metadata"] = metadata
    artifacts["numeric_features"] = metadata["features"]["numeric"]

    logger.info("Successfully loaded SVM pipeline and metadata!")
    yield
    artifacts.clear()
    logger.info("Cleaned up model artifacts from memory.")


app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="Production REST API for real-time transaction risk scoring using LinearSVC.",
    version="1.0.0",
    lifespan=lifespan,
)


# ============================================================
# SCHEMAS (Request & Response Validation)
# ============================================================
class TransactionInput(BaseModel):
    """Schema validating incoming transaction feature payload."""

    V1: float = Field(..., example=-1.359807)
    V2: float = Field(..., example=-0.072781)
    V3: float = Field(..., example=2.536347)
    V4: float = Field(..., example=1.378155)
    V5: float = Field(..., example=-0.338321)
    V6: float = Field(..., example=0.462388)
    V7: float = Field(..., example=0.239599)
    V8: float = Field(..., example=0.098698)
    V9: float = Field(..., example=0.363787)
    V10: float = Field(..., example=0.090794)
    V11: float = Field(..., example=-0.551600)
    V12: float = Field(..., example=-0.617801)
    V13: float = Field(..., example=-0.991390)
    V14: float = Field(..., example=-0.311169)
    V15: float = Field(..., example=1.468177)
    V16: float = Field(..., example=-0.470401)
    V17: float = Field(..., example=0.207971)
    V18: float = Field(..., example=0.025791)
    V19: float = Field(..., example=0.403993)
    V20: float = Field(..., example=0.251412)
    V21: float = Field(..., example=-0.018307)
    V22: float = Field(..., example=0.277838)
    V23: float = Field(..., example=-0.110474)
    V24: float = Field(..., example=0.066928)
    V25: float = Field(..., example=0.128539)
    V26: float = Field(..., example=-0.189115)
    V27: float = Field(..., example=0.133558)
    V28: float = Field(..., example=-0.021053)
    Amount: float = Field(..., ge=0.0, example=149.62)


class PredictionResponse(BaseModel):
    """Schema for prediction output."""

    is_fraud: bool
    label: str
    decision_score: float
    status: str


class HealthResponse(BaseModel):
    """Schema for system status endpoint."""

    status: str
    model_algorithm: str
    model_created_at: str


# ============================================================
# API ENDPOINTS
# ============================================================
@app.get("/health", response_model=HealthResponse, tags=["System"])
def health_check():
    """System readiness check."""
    if "model" not in artifacts:
        raise HTTPException(
            status_code=status.HTTP_530_SERVICE_UNAVAILABLE,
            detail="Model pipeline not loaded",
        )
    return {
        "status": "healthy",
        "model_algorithm": artifacts["metadata"]["model"]["algorithm"],
        "model_created_at": artifacts["metadata"]["created_at"],
    }


@app.post("/predict", response_model=PredictionResponse, tags=["Inference"])
def predict_fraud(payload: TransactionInput):
    """Accept single transaction and return real-time fraud assessment."""
    try:
        model = artifacts["model"]
        expected_features = artifacts["numeric_features"]

        # Convert input Pydantic model to Pandas DataFrame
        input_data = payload.model_dump()
        df_input = pd.DataFrame([input_data])[expected_features]

        # Single pass prediction + confidence margin evaluation
        raw_pred = int(model.predict(df_input)[0])
        decision_score = float(model.decision_function(df_input)[0])

        is_fraud = raw_pred == 1
        label = "Fraudulent" if is_fraud else "Legitimate"
        recommendation = (
            "Flag for manual verification" if is_fraud else "Approve transaction"
        )

        return {
            "is_fraud": is_fraud,
            "label": label,
            "decision_score": round(decision_score, 4),
            "status": recommendation,
        }

    except Exception as exc:
        logger.error("Inference exception: %s", str(exc), exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Inference error: {str(exc)}",
        )
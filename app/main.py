from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.model import load_artifacts, predict_price
from app.schema import CarFeatures, PredictionResponse


app = FastAPI(
    title="Car Price Prediction API",
    version="1.0"
)


@app.on_event("startup")
def startup_event():
    load_artifacts()


@app.get("/")
def test():
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Car Price Prediction API is running"
        }
    )


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(features: CarFeatures):
    price = predict_price(
        features.model_dump(mode="json")
    )

    return PredictionResponse(
        prediction_price=price
    )
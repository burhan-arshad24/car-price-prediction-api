from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "random_forest_model.pkl"
COLS_PATH = BASE_DIR / "feature_columns.pkl"

print("Model path:", MODEL_PATH)
print("Feature columns path:", COLS_PATH)


_model = None
_feature_columns = None


def load_artifacts():
    global _model, _feature_columns

    if _model is None:
        _model = joblib.load(MODEL_PATH)

    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)


def preprocess(payload: dict) -> pd.DataFrame:
    load_artifacts()

    df = pd.DataFrame([payload])

    categorical_cols = [
        "Fuel_Type",
        "Seller_Type",
        "Transmission",
        "Owner",
        "Car_Name"
    ]

    df_encoded = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    for column in _feature_columns:
        if column not in df_encoded.columns:
            df_encoded[column] = 0

    df_encoded = df_encoded[_feature_columns]

    return df_encoded


def predict_price(payload: dict) -> float:
    load_artifacts()

    X = preprocess(payload)

    prediction = _model.predict(X)[0]

    return float(prediction)
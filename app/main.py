from app.models import ForecastInput, ForecastOutput, ModelParams, ModelPerformance
from fastapi import FastAPI
import pandas as pd
import numpy as np
from prophet.serialize import model_from_json

app = FastAPI()

# load model from the json
with open("../models/prophet-model.json", "r") as fin:
    model = model_from_json(fin.read())


@app.post("/forecast", response_model=ForecastOutput)
def get_forecast(forecast_input: ForecastInput):
    """
    Generates a forecast for a single timestamp.

    Args:
    forecast_input (dict): Dictionary with 'year' and 'month' keys.

    Returns:
    dict: Prediction for the requested timestamp.
    """
    year = forecast_input["year"]
    month = forecast_input["month"]

    future = model.make_future_dataframe(periods=1, freq="M")
    future["ds"] = pd.to_datetime(f"{year}-{month}-01")
    forecast = model.predict(future)
    return {"prediction": forecast["yhat"].values[0]}


@app.get("/model-performance", response_model=ModelPerformance)
def get_model_performance():
    """
    Calculates performance metrics for the Prophet model.

    Returns:
    dict: Model performance metrics, including RMSE and R2 score.
    """
    return {"rmse": "", "r2": ""}


@app.get("/model-params", response_model=ModelParams)
def get_model_params():
    # ...
    return {
        "growth": model.growth,
        "changepoint_prior_scale": model.changepoint_prior_scale,
        "seasonality_prior_scale": model.seasonality_prior_scale,
        "seasonality_mode": model.seasonality_mode,
    }

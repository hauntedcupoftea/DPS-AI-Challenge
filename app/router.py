"""all fastapi routers go here"""

from fastapi import APIRouter
from prophet.serialize import model_from_json
from app.functions import *
from app.models import *

# load model from the json
with open("./models/prophet-model.json", "r") as fin:
    model = model_from_json(fin.read())


forecaster = APIRouter(prefix="/forecast", tags=["forecast", "predict"])
model_stats = APIRouter(prefix="/model", tags=["statistics", "model statistics"])


@forecaster.post("/", response_model=ForecastOutput)
def get_forecast(forecast_input: ForecastInput):
    """
    Generates a forecast for a single timestamp.

    Args:
    forecast_input (dict): Dictionary with 'year' and 'month' keys.

    Returns:
    dict: Prediction for the requested timestamp.
    """
    return forecast(forecast_input=forecast_input, model=model)


@model_stats.get("/performance", response_model=ModelPerformance)
def get_model_performance():
    """
    Calculates performance metrics for the Prophet model.

    Returns:
    dict: Model performance metrics, including RMSE and R2 score.
    """
    return model_performance()


@model_stats.get("/params", response_model=ModelParams)
def get_model_params():
    """
    Returns the current parameters used in the Prophet model.

    Returns:
    dict: Model parameters.
    """
    return model_params()

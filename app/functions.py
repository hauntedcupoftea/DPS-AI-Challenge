import pandas as pd

from app.models import ForecastInput


def forecast(forecast_input: ForecastInput, model):
    year = forecast_input.year
    month = forecast_input.month

    future = model.make_future_dataframe(periods=1, freq="M")
    future["ds"] = pd.to_datetime(f"{year}-{month}-01")
    forecast = model.predict(future)
    return {"prediction": forecast["yhat"].values[0]}


def model_performance():
    return {
        "mae": 7.8796157260626245,
        "rmse": 9.679660884189174,
        "r2": 0.5418296585188169,
    }


def model_params():
    return {
        "growth": "linear",
        "changepoint_prior_scale": 0.2,
        "seasonality_prior_scale": 1.0,
        "seasonality_mode": "multiplicative",
    }

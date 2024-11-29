import pandas as pd


def forecast(forecast_input, model):
    year = forecast_input["year"]
    month = forecast_input["month"]

    future = model.make_future_dataframe(periods=1, freq="M")
    future["ds"] = pd.to_datetime(f"{year}-{month}-01")
    forecast = model.predict(future)
    return {"prediction": forecast["yhat"].values[0]}


def model_performance():
    return {"rmse": "", "r2": ""}


def model_params():
    return {
        "growth": "",
        "changepoint_prior_scale": "",
        "seasonality_prior_scale": "",
        "seasonality_mode": "",
    }

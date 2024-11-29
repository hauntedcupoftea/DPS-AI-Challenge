"""A collection of schemas that define JSON Schema for Responses and Queries"""

from pydantic import BaseModel, Field


class ForecastInput(BaseModel):
    year: int = Field(examples=[2014, 2010])
    month: int = Field(examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


class ForecastOutput(BaseModel):
    prediction: float


class ModelPerformance(BaseModel):
    mae: float
    rmse: float
    r2: float


class ModelParams(BaseModel):
    growth: str
    changepoint_prior_scale: float
    seasonality_prior_scale: float
    seasonality_mode: str

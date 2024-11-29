from app.models import ModelParams, ModelPerformance
from app.router import forecaster, model_stats
from fastapi import FastAPI

app = FastAPI()
app.include_router(forecaster)
app.include_router(model_stats)

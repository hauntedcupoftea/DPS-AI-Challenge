from app.models import ModelParams, ModelPerformance
from app.router import forecaster, model_stats
from fastapi import FastAPI

app = FastAPI()
app.include_router(forecaster)
app.include_router(model_stats)


@app.get("/")
def hello():
    return {"message": "Welcome to the AI-Challenge forecaster"}


def start():
    """Launched with `poetry run start` at root level"""
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)

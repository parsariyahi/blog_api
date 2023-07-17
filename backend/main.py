from fastapi import FastAPI

from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


@app.get("/")
def index():
    return {"msg": "hello world"}
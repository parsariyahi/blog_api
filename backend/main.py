from fastapi import FastAPI
from uvicorn import run

from apis.base import api_router
from core.config import settings
from db.session import engine
from db.base import Base



def create_tables():         
	Base.metadata.create_all(bind=engine)
        
def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)
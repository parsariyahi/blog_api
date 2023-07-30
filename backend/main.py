import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute

from apis.base import api_router
from core.config import settings
from db.session import engine
from db.base import Base



def create_tables():         
	Base.metadata.create_all(bind=engine)
        
def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION, debug=settings.DEBUG)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def api_lists():
    all_routes = app.routes
    api_routes = []
    for route in all_routes:
        if isinstance(route, APIRoute):
            print(route.path)
            api_routes.append({
                "path": route.path,
                "name": route.name,
                "methods": route.methods,
            })
    return {"routes": api_routes}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
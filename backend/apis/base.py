from fastapi import APIRouter

# from apis.v1.user_routes import router as user_router
# from apis.v1.blog_routes import  router as blog_router
from apis.v1 import blog_routes, user_routes


api_router = APIRouter()

api_router.include_router(user_routes.router,prefix="/users",tags=["users"])
api_router.include_router(blog_routes.router,prefix="/blogs",tags=["blogs"])
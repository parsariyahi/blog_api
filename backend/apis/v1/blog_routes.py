from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from db.base import User as UserModel
from db.repository.blog import create_blog, retrive_blog, update_blog, delete_blog, list_blogs
from schemas.blog import BlogShow, Blog as BlogSchema
from apis.utils.user import get_current_user
from apis.exceptions import HttpBlogNotFound, HttpBlogAuthorNotMatch
from db.exceptions import BlogAuthorNotAllowed, BlogDoesNotExists

router = APIRouter()

@router.post("/add", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def publish_blog(blog: BlogSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    blog = create_blog(blog, current_user.id, db)

    return blog

@router.get("/{blog_id}/get", response_model=BlogShow, status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    try:

        blog = retrive_blog(blog_id, db)

    except BlogDoesNotExists:
        raise HttpBlogNotFound()

    return blog

@router.put("/{blog_id}/edit", response_model=BlogShow, status_code=status.HTTP_200_OK)
def edit_blog(blog_id: int, blog: BlogSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    try:

        blog = update_blog(blog_id, blog, current_user.id, db)

    except BlogDoesNotExists:
        raise HttpBlogNotFound()

    except BlogAuthorNotAllowed:
        raise HttpBlogAuthorNotMatch()

    return blog

@router.delete("/{blog_id}/delete", status_code=status.HTTP_200_OK)
def remove_blog(blog_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    try:

        result = delete_blog(blog_id, current_user.id, db)

    except BlogDoesNotExists:
        raise HttpBlogNotFound()

    except BlogAuthorNotAllowed:
        raise HttpBlogAuthorNotMatch()

    return {"msg": f"The Blog with id: {blog_id} deleted"}


@router.get("/all", response_model=List[BlogShow], status_code=status.HTTP_200_OK)
def list_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db)

    return blogs
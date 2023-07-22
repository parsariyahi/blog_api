from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.blog import create_blog, retrive_blog, update_blog, delete_blog, list_blogs
from schemas.blog import BlogShow, Blog as BlogSchema

router = APIRouter()

@router.post("/add", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def publish_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    blog = create_blog(blog, db, author_id=1)

    return blog

@router.get("/{blog_id}/get", response_model=BlogShow, status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = retrive_blog(blog_id, db)

    if not blog:
        raise HTTPException(detail=f"Blog with id: {blog_id} does not exists", status_code=status.HTTP_404_NOT_FOUND)

    return blog

@router.put("/{blog_id}/edit", response_model=BlogShow, status_code=status.HTTP_200_OK)
def edit_blog(blog_id: int, blog: BlogSchema, db: Session = Depends(get_db)):
    blog = update_blog(blog_id, blog, 1, db)

    if not blog:
        raise HTTPException(detail=f"Blog with id: {blog_id} does not exists", status_code=status.HTTP_404_NOT_FOUND)

    return blog

@router.delete("/{blog_id}/delete", status_code=status.HTTP_200_OK)
def remove_blog(blog_id: int, db: Session = Depends(get_db)):
    result = delete_blog(blog_id, db)

    if not result:
        raise HTTPException(detail=f"Blog with id: {blog_id} does not exists", status_code=status.HTTP_404_NOT_FOUND)

    return {"msg": f"The Blog with id: {blog_id} deleted"}


@router.get("/all", response_model=List[BlogShow], status_code=status.HTTP_200_OK)
def list_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db)

    return blogs
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.blog import create_blog, retrive_blog
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
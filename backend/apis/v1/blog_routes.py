from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.blog import create_blog
from schemas.blog import BlogShow, Blog as BlogSchema

router = APIRouter()

@router.post("/add", response_model=BlogShow, status_code=status.HTTP_201_CREATED)
def publish_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    blog = create_blog(blog, db, author_id=1)

    return blog
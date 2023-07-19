from sqlalchemy.orm import Session

from schemas.blog import Blog as BlogSchema
from db.base import Blog as BlogModel


def create_blog(blog: BlogSchema, db: Session, author_id: int = 1):
    blog = BlogModel(**blog.dict(), author_id=author_id)

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog
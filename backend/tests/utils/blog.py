from typing import Optional
from sqlalchemy.orm import Session

from db.repository.blog import create_blog, retrive_blog
from db.exceptions import BlogDoesNotExists
from db.base import User as UserModel, Blog as BlogModel
from schemas.blog import Blog as BlogSchema
from tests.utils.user import create_random_user


def create_random_blog(db: Session, user: Optional[UserModel | None] = None):
    blog = BlogSchema(
        title="test blog",
        content="this is a test blog",
    )

    if not user:
        user = create_random_user(db)

    blog = create_blog(blog, user.id, db)

    return blog 

def blog_exists(db: Session, blog: BlogModel):
    try:
        blog = retrive_blog(blog.id, db)
        return True

    except BlogDoesNotExists:
        return False
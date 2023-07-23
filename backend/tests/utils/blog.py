from sqlalchemy.orm import Session

from db.repository.blog import create_blog
from schemas.blog import Blog as BlogSchema
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    blog = BlogSchema(
        title="test blog",
        content="this is a test blog",
    )
    user = create_random_user(db)

    blog = create_blog(blog, db, author_id=user.id)

    return blog 

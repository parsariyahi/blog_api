from sqlalchemy.orm import Session

from schemas.blog import Blog as BlogSchema
from db.base import Blog as BlogModel
from db.exceptions import BlogAuthorNotAllowed, BlogDoesNotExists


def create_blog(blog: BlogSchema, author_id: int, db: Session):
    blog = BlogModel(**blog.model_dump(), author_id=author_id)

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog

def retrive_blog(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()

    if not blog:
        raise BlogDoesNotExists()

    return blog

def update_blog(blog_id, blog: BlogSchema, author_id: int, db: Session):
    db_blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()

    if not db_blog:
        raise BlogDoesNotExists()

    if db_blog.author_id != author_id:
        raise BlogAuthorNotAllowed()

    db_blog.title = blog.title
    db_blog.content = blog.content

    db.add(db_blog)
    db.commit()

    return db_blog

def delete_blog(blog_id: int, author_id, db: Session) -> bool:
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id)

    if not blog.first():
        raise BlogDoesNotExists()

    if blog.first().author_id != author_id:
        raise BlogAuthorNotAllowed()

    blog.delete()
    db.commit()

    return True

def list_blogs(db: Session):
    blogs = db.query(BlogModel).filter(BlogModel.is_active == True).all()

    return blogs
from sqlalchemy.orm import Session

from schemas.blog import Blog as BlogSchema
from db.base import Blog as BlogModel


def create_blog(blog: BlogSchema, db: Session, author_id: int = 1):
    blog = BlogModel(**blog.model_dump(), author_id=author_id)

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog

def retrive_blog(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()

    return blog

def update_blog(blog_id, blog: BlogSchema, author_id: int, db: Session):
    db_blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()

    if not db_blog:
        return

    db_blog.title = blog.title
    db_blog.content = blog.content

    db.add(db_blog)
    db.commit()

    return db_blog

def delete_blog(blog_id: int, db: Session) -> bool:
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id)

    if not blog.first():
        return False

    blog.delete()
    db.commit()

    return True

def list_blogs(db: Session):
    blogs = db.query(BlogModel).filter(BlogModel.is_active == True).all()

    return blogs
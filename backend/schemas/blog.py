from typing import Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime

class Blog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    # @root_validator(pre=True)
    @validator("slug", pre=True)
    def generate_slug(cls, slug, values):
        title = values.get("title", "")
        slug = None
        if title:
            slug = title.replace(" ", "-").lower()

        return slug

class BlogShow(BaseModel):
    title: str
    slug: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
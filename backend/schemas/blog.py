from typing import Optional
from pydantic import BaseModel, root_validator, Field
from datetime import datetime

class Blog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()

        return values

class BlogShow(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
from typing import Optional
from pydantic import BaseModel, field_validator, FieldValidationInfo, Field, ConfigDict
from datetime import datetime

class Blog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    # @root_validator(pre=True)
    @field_validator("slug", mode="before")
    def generate_slug(cls, slug, info: FieldValidationInfo):
        title = info.get("title", "")
        slug = None
        if title:
            slug = title.replace(" ", "-").lower()

        return slug

class BlogShow(BaseModel):
    title: str
    slug: str
    content: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True
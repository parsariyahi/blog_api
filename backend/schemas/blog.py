from typing import Optional
from pydantic import BaseModel, field_validator, FieldValidationInfo, ValidationError, ConfigDict, model_validator
from datetime import datetime

class Blog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    # @root_validator(pre=True)
    @model_validator(mode="before")
    def generate_slug(cls, values):
        if not ("slug" in values):

            title = values.get("title", None)

            if not title:
                raise ValidationError("title is empty, we cant generate slug")

            values["slug"] = title.replace(" ", "-")

        return values

class BlogShow(BaseModel):
    title: str
    slug: str
    content: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True
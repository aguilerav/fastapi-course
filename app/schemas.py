from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    """Schema for a post object returned by the API."""

    id: int
    created_at: datetime

    class Config:
        """Pydantic configuration to allow ORM mode."""

        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):

    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """Pydantic configuration to allow ORM mode."""

        from_attributes = True

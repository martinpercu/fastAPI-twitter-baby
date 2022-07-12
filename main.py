# Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    
class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=80
    )
    
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=48
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=48
    )
    birth_date: Optional[date] = Field(default=None)
    

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_moment: datetime = Field(default=datetime.now)
    updated_moment: Optional[datetime] = Field(defautl=None)
    created_by: User = Field(...)


@app.get(path="/")
def home():
    return {"baby-twitter": "Working OK and Happy"}
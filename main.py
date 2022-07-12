# Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


# FastAPI
from fastapi import FastAPI
from fastapi import status

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

# Path Operation

@app.get(path="/")
def home():
    return {"baby-twitter": "Working OK and Happy"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register the user",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Login the user",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all the users",
    tags=["Users"]
)
def show_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show the user",
    tags=["Users"]
)
def show_the_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete the user",
    tags=["Users"]
)
def delete_the_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update the user",
    tags=["Users"]
)
def update_the_user():
    pass


## Tweets


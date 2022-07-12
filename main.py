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
    created_moment: datetime = Field(default=datetime.now())
    updated_moment: Optional[datetime] = Field(defautl=None)
    created_by: User = Field(...)

# Path Operation

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register the user",
    tags=["Users"]
)
def signup():
    pass

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Login the user",
    tags=["Users"]
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all the users",
    tags=["Users"]
)
def show_all_users():
    pass

### Show the user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show the user",
    tags=["Users"]
)
def show_one_user():
    pass

### Delete the user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete the user",
    tags=["Users"]
)
def delete_the_user():
    pass

### Update the user
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

## Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all the tweets",
    tags=["Tweets"]
)
def home():
    return {"baby-twitter": "Working OK and Happy"}

### Post a tweets
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass


### Show a tweets
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweets
@app.get(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweets
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass

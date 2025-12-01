from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event  

class User(BaseModel):
    email: EmailStr
    username: str
    password: str
    events: Optional[List[Event]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }

class NewUser(User):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "password": "strong_password123",
                "events": [],
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong_password123",
            }
        }
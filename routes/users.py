from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["Users"])
users = {}

@user_router.post("/signup")
async def sign_new_user(data: User):
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    users[data.email] = data
    return {"message": "User successfully registered"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn):
    if user.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if users[user.email].password != user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials")
    return {"message": "User signed in successfully"}

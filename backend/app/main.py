from fastapi import FastAPI, Header, HTTPException, Response
import uvicorn
from mongoengine import connect
from envparse import Env
from fastapi.middleware.cors import CORSMiddleware
from typing import Union

from models import *
from shemas import *

import crud


env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/test_database")

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", description="Root endpoint")
async def root():
    return {"message": "Hello, World!"}

@app.get("/api", description="Root endpoint")
async def roott(token: str = None):
    
    return {"message": f"Hlo,  = , {token}"}

@app.post("/api", description="hz Root endpoint")
async def roott(token: str = None):
    
    return {"message": f"Hlo,  = , {token}"}


ApiPrefix = "/api/v1"

@app.post(f"{ApiPrefix}/register", description="Register endpoint")
async def register(user: CreateUser):
    try:
        new_user = crud.regidtration(user.name, user.surname, user.login, user.email, user.password)
        if new_user:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}
    
@app.post(f"{ApiPrefix}/login", description="Login endpoint")
async def login(login_user: LoginUser):
    try:
        user = crud.login(login_user.email, login_user.password)
        if user:
            return {"status": 200, "tocken": crud.get_tocken(user)}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


@app.get(f"{ApiPrefix}/user", description="Get user endpoint")
async def get_user(get_user: GetUser):
    try:
        user = User.objects(login=get_user.login).first()
        if user:
            return {"status": 200, "user": user.json_convert()}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


@app.put(ApiPrefix + "/user/{login}", description="Update user endpoint")
async def update_user(update_user: UpdateUser):
    try:
        user = crud.update_user(update_user.name, update_user.surname, update_user.login)
        if user:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


connect(host=MONGODB_URL)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

from fastapi import FastAPI, Request
import uvicorn
from mongoengine import connect
from envparse import Env

from models import *
import crud


env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017/test_database")

app = FastAPI()


@app.get("/", description="Root endpoint")
async def root():
    return {"message": "Hello, World!"}

@app.get("/api", description="Root endpoint")
async def roott():
    return {"message": "Hello, World!"}

ApiPrefix = "/api/v1"

@app.post(f"{ApiPrefix}/register", description="Register endpoint")
async def register(name: str, surname: str, login: str, email: str, password: str):
    try:
        new_user = crud.regidtration(name, surname, login, email, password)
        if new_user:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}
    
@app.post(f"{ApiPrefix}/login", description="Login endpoint")
async def login(email: str, password: str):
    try:
        user = crud.login(email, password)
        if user:
            return {"status": 200, "tocken": crud.get_tocken(user)}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


@app.get(f"{ApiPrefix}/user", description="Get user endpoint")
async def get_user(tocken: str):
    try:
        user = User.objects(tocken=tocken).first()
        if user:
            return {"status": 200, "user": user.json_convert()}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}
    

@app.put(ApiPrefix + "/user/{login}", description="Update user endpoint")
async def update_user(name: str, surname: str, login: str):
    try:
        user = crud.update_user(name, surname, login)
        if user:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


connect(host=MONGODB_URL)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
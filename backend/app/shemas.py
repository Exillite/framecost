from pydantic import BaseModel

class Test(BaseModel):
    token: str

class CreateUser(BaseModel):
    name: str
    surname: str
    login: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class GetUser(BaseModel):
    token: str
    login: str

class UpdateUser(BaseModel):
    token: str
    name: str
    surname: str
    login: str

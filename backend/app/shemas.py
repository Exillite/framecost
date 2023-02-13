from pydantic import BaseModel

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
    login: str

class UpdateUser(BaseModel):
    name: str
    surname: str
    login: str

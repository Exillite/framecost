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
    name: str
    surname: str
    

class CreateShop(BaseModel):
    title: str
    
    
class CreateProduct(BaseModel):
    title: str
    category: str
    price: float
    shop_id: str




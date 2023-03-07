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


class AddAdmin(BaseModel):
    email: str

class CreateShop(BaseModel):
    title: str
    
    
class CreateProduct(BaseModel):
    title: str
    category: str
    price: float
    slug: str
    coef: float
    shop_id: str

class UpdateProduct(BaseModel):
    title: str
    category: str
    price: float


class CreateItem(BaseModel):
    product_id: str
    params: str
    
class UpdateItem(BaseModel):
    params: str
    

class CreateTemplate(BaseModel):
    title: str
    shop_id: str
    products: str
    

class CreateOrder(BaseModel):
    shop_id: str
    items: str


class Template_Price(BaseModel):
    data: str

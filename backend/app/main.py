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


def is_login(token: str, user_id: str) -> User:
    try:
        if not token or not user_id:
            return None
        usr = User.objects(pk=user_id[1:-1]).first()
        print(usr.email)
        if not usr:
            return None
        print(str(token), str(usr.email))
        if crud.check_password(str(usr.email), str(token[1:-1])):
            return usr
    except Exception as e:
        print(e)
        return None
    
def permision_check(user: User, shop: Shop) -> bool:
    if shop.owner == user:
        return True
    elif user in shop.admins:
        return True
    else:
        return False


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
            return {"status": 200, "tocken": crud.get_tocken(user), "user_id": str(user.pk)}
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
async def update_user(update_user: UpdateUser, login: str):
    try:
        user = crud.update_user(update_user.name, update_user.surname, login)
        if user:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}
    
    
@app.post(ApiPrefix + "/shop", description="Create new shop endpoint")
async def create_shop(new_shop: CreateShop, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    try:
        shop = crud.create_shop(new_shop.title, user)
        if shop:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}    


@app.get(ApiPrefix + "/shop/{shop_slug}", description="Get shop endpoint")
async def get_shop(shop_slug: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    
    try:
        shop = Shop.objects(slug=shop_slug).first()
        if not shop:
            return {"status": 400}
        if not permision_check(user, shop):
            return {"status": 400}
        
        return {"status": 200, "shop": shop.json_convert()}
    except Exception as e:
        return {"status": 500}


@app.get(ApiPrefix + "/user/shops", description="Get all user shops endpoint")
async def get_users_shops(token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    
    try:
        print(user.email)
        shops = Shop.objects(admins__contains=user)
        shops_list = []
        
        for shop in shops:
            shops_list.append(shop.json_convert())
            
        shops = Shop.objects(owner=user)
        for shop in shops:
            shops_list.append(shop.json_convert())
            
        return {"status": 200, "shops": shops_list}
    except Exception as e:
        print(e)
        return {"status": 500}


@app.post(ApiPrefix + "/product")
async def create_product(prod: CreateProduct, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = Shop.objects(pk=prod.shop_id).first()
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        product = crud.create_product(prod.title, prod.category, prod.price, shop)
        if product:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


@app.get(ApiPrefix + "/shop/{shop_slug}/products")
async def get_shops_products(shop_slug: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = Shop.objects(slug=shop_slug).first()
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        prods = crud.get_products_by_shop(shop)
        prods_lst = []
        
        for p in prods:
            prods_lst.append(p.json_convert())
        
        return {"status": 200, "products": prods_lst}
    except Exception as e:
        return {"status": 500}


@app.get(ApiPrefix + "/product/{product_slug}")
async def get_product(product_slug: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    prd = crud.get_product(product_slug)
    shop = prd.shop
    if not prd:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}

    try:
        return {"status": 200, "product": prd.json_convert()}
    except Exception as e:
        return {"status": 500}
    
    
@app.put(ApiPrefix + "/product/{product_slug}")
async def update_product(edit_prd: UpdateProduct, product_slug, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    prd = crud.get_product(product_slug)
    shop = prd.shop
    if not prd:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}

    try:
        updd_prd = crud.update_product(edit_prd.title, edit_prd.category, edit_prd.price, product_slug)
        if updd_prd:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


connect(host=MONGODB_URL)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

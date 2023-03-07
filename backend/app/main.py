from fastapi import FastAPI
import uvicorn
from mongoengine import connect
from envparse import Env
from fastapi.middleware.cors import CORSMiddleware
from typing import Union

from models import *
from shemas import *

from templates import *

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
    

@app.post(ApiPrefix + "/shop/{shop_slug}/admin")
async def add_new_admin(shop_slug: str, new_admin: AddAdmin, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    
    try:
        shop = Shop.objects(slug=shop_slug).first()
        if not shop:
            return {"status": 400}
        if not permision_check(user, shop):
            return {"status": 400}
        
        crud.add_admin_to_shop(shop_slug, new_admin.email)
        
        return {"status": 200}

    except Exception as e:
        return {"status": 500} 


@app.get(ApiPrefix + "/user/shops", description="Get all user shops endpoint")
async def get_users_shops(token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    
    try:
        shops = crud.get_users_shops(user)
        
        shops_list = []
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
        product = crud.create_product(prod.title, prod.category, prod.price, prod.slug, prod.coef, shop)
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
            print(1)
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
    
    
@app.delete(ApiPrefix + "/product/{product_slug}")
async def delete_product(product_slug: str, token: str = None, user_id: str = None):
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
        crud.delete_product(product_slug)
        return {"status": 200}
    except Exception as e:
        return {"status": 500}
    
    
@app.put(ApiPrefix + "/product/{product_slug}")
async def update_product(edit_prd: UpdateProduct, product_slug: str, token: str = None, user_id: str = None):
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
        updd_prd = crud.update_product(edit_prd.title, edit_prd.category, edit_prd.price, product_slug, edit_prd.coef)
        if updd_prd:
            return {"status": 200}
        else:
            return {"status": 400}
    except Exception as e:
        return {"status": 500}


@app.get(ApiPrefix + "/item/{item_id}")
async def get_item(item_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    item = crud.get_item_by_id(item_id)
    prd = item.product
    shop = prd.shop
    if not item:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        return {"status": 200, "item": item.json_convert()}
    except Exception as e:
        return {"status": 500}
    
    
@app.delete(ApiPrefix + "/item/{item_id}")
async def delete_item(item_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    item = crud.get_item_by_id(item_id)
    prd = item.product
    shop = prd.shop
    if not item:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        crud.delete_item(item_id)
        return {"status": 200}
    except Exception as e:
        return {"status": 500}


@app.post(ApiPrefix + "/item")
async def create_item(new_item: CreateItem, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    prd = crud.get_product_by_id(new_item.product_id)
    shop = prd.shop
    if not prd:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        prms = crud.params_pars(new_item.params)
        lst = []
        if prms['cnt'] >= 1:
            lst.append(prms['a'])
        if prms['cnt'] == 2:
            lst.append(prms['b'])
            
                
        item = crud.create_item(prd, prms['cnt'], lst)
        if not item:
            return {"ststus": 400}
        
        return {"status": 200}
    except Exception as e:
        print(e)
        return {"status": 500, "error": str(e)}


@app.put(ApiPrefix + "/item/{item_id}")
async def update_item(item_id: str, edit_itm: UpdateItem, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    item = crud.get_item_by_id(item_id)
    prd = item.product
    shop = prd.shop
    if not item:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        prms = crud.params_pars(edit_itm.params)
        lst = []
        if prms['cnt'] >= 1:
            lst.append(prms['a'])
        if prms == 2:
            lst.append(prms['b'])

        updd_item = crud.update_item(prms['cnt'], lst, str(item.pk))
        if not updd_item:
            return {"status": 400}
        else:
            return {"status": 200}
        
    except Exception as e:
        return {"status":500}


@app.get(ApiPrefix + "/product/{product_slug}/items")
async def get_all_products_items(product_slug: str, token: str = None, user_id: str = None):
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
        items = crud.get_items_by_product(prd)
        if not items:
            return {"status": 400}
        items_lst = []
        for itm in items:
            items_lst.append(itm.json_convert())
        
        return {"status": 200, "items": items_lst}
    except Exception as e:
        return {"status": 500}
    

@app.post(ApiPrefix + "/template")
async def create_template(new_teplate: CreateTemplate, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = crud.get_shop_by_id(new_teplate.shop_id)
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        tmpl = crud.create_template(new_teplate.title, crud.get_shop_by_id(new_teplate.shop_id), crud.products_pars(new_teplate.products))
        if not tmpl:
            return {"status": 400}
        return {"status": 200}
    except Exception as e:
        return {"status": 500}
    

@app.get(ApiPrefix + "/shop/{shop_slug}/templates")
async def get_shops_templates(shop_slug: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = crud.get_shop(shop_slug)
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        templs = crud.get_templates_by_shop(shop)
        templs_lst = []
        print(templs)
        for tmpl in templs:
            print(tmpl)
            templs_lst.append(tmpl.json_convert())
            
        if not templs_lst:
            return {"status": 400}
        else:
            return {"status": 200, "templates": templs_lst}
    except Exception as e:
        return {"status": 500}
    

@app.get(ApiPrefix + "/template/{template_id}")
async def get_template(template_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    tmpl = crud.get_template_by_id(template_id)
    shop = tmpl.shop
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        return {"status": 200, "template": tmpl.json_convert()}
    except Exception as e:
        return {"status": 500}
    
    
@app.delete(ApiPrefix + "/template/{template_id}")
async def delete_template(template_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    tmpl = crud.get_template_by_id(template_id)
    shop = tmpl.shop
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        crud.delete_template(template_id)
        return {"status": 200}
    except Exception as e:
        return {"status": 500}


@app.post(ApiPrefix + "/order")
async def create_order(new_order: CreateOrder, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = crud.get_shop_by_id(new_order.shop_id)
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        order = crud.create_order(shop, new_order.items)
        if not order:
            return {"status": 400}
        else:
            return {"status": 200}
    except Exception as e:
        return {"status": 500, "error": str(e)}
    
    
@app.post(ApiPrefix + "/order/price")
async def calculate_order_price(new_order: CreateOrder, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = crud.get_shop_by_id(new_order.shop_id)
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}
    
    try:
        price = crud.order_price(shop, new_order.items)
        return {"status": 200, "price": price}
    except Exception as e:
        return {"status": 500, "error": str(e)}
    
    
@app.get(ApiPrefix + "/order/{order_id}")
async def get_order(order_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    order = crud.get_order_by_id(order_id)
    shop = order.shop.pk
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}

    try:
        return {"status": 200, "order": order.json_convert()}
    except Exception as e:
        return {"status": 500, "error": str(e)}
    
    
@app.delete(ApiPrefix + "/order/{order_id}")
async def delete_order(order_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    order = crud.get_order_by_id(order_id)
    shop = order.shop.pk
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}

    try:
        crud.delete_order(order_id)
        return {"status": 200}
    except Exception as e:
        return {"status": 500}
    
    
@app.get(ApiPrefix + "/shop/{shop_id}/orders")
async def get_shops_orders(shop_id: str, token: str = None, user_id: str = None):
    user = is_login(token, user_id)
    if not user:
        return {"status": 400}
    shop = crud.get_shop_by_id(shop_id)
    if not shop:
        return {"status": 400}
    if not permision_check(user, shop):
        return {"status": 400}

    try:
        orders = crud.get_orders_by_shop(shop)
        orders_lst = []
        for el in orders:
            orders_lst.append(el.json_convert())
            
        if not orders_lst:
            return {"status": 400}
        
        return {"status": 200, "orders": orders_lst}
    except Exception as e:
        return {"status": 500, "error": str(e)}
    

@app.post(ApiPrefix + "/price/{template}")
async def get_templat_prices(template: str, tmpp: Template_Price):
    data = json.loads(tmpp.data)
    print(data)
    if template == "WithOut_Paspartu":
        tmpl = WithOut_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget_width"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "With_Paspartu":
        tmpl = With_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget_width"], data["paspartu_width"])
        return {"status": 200, "data": tmpl.get_data()}
    
    elif template == "Rama_With_Cant":
        tmpl = Rama_With_Cant(data["width"], data["height"], data["is_horisontal"], data["baget_width"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "Double_Rama":
        tmpl = Double_Rama(data["width"], data["height"], data["is_horisontal"], data["baget1_width"], data["baget2_width"])
        return {"status": 200, "data": tmpl.get_data()}
    
    elif template == "Rama_With_Natazka_Na_Podramnik":
        tmpl = Rama_With_Natazka_Na_Podramnik(data["width"], data["height"], data["is_horisontal"], data["baget_width"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "Double_Rama_With_Paspartu":
        tmpl = Double_Rama_With_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget1_width"], data["baget2_width"], data["paspartu_width"])
        return {"status": 200, "data": tmpl.get_data()}

    elif template == "Rama_With_Cant_And_Single_Paspartu":
        tmpl = Rama_With_Cant_And_Single_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget_width"], data["paspartu_width"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "Rama_With_Cant_And_Double_Paspartu":
        tmpl = Rama_With_Cant_And_Double_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget_width"], data["paspartu_width"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "Volume_Dezigne":
        tmpl = Volume_Dezigne(data["width"], data["height"], data["is_horisontal"], data["baget_width"], data["baget_height"])
        return {"status": 200, "data": tmpl.get_data()}
        
    elif template == "Volume_Dezigne_With_Paspartu":
        tmpl = Volume_Dezigne_With_Paspartu(data["width"], data["height"], data["is_horisontal"], data["baget_width"], data["baget_height"], data["paspartu_width"])
        return {"status": 200, "data": tmpl.get_data()}
    
    else:
        return {"status": 400}

connect(host=MONGODB_URL)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

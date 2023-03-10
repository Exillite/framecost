from models import User, Shop, Product, Item, Template, Order
from mongoengine.queryset.visitor import Q

import bcrypt
from slugify import slugify
import datetime
import json

def get_hashed_password(plain_text_password: str) -> str:
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password: str, hashed_password: str) -> bool:
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


def regidtration(name: str, surname: str, login: str, email: str, password: str) -> User:
    # Check if user exists
    if User.objects(email=email).first():
        return None
    if User.objects(login=login).first():
        return None
    
    user = User(name=name, surname=surname, email=email, password=get_hashed_password(password), role="user", is_active=True, login=login)
    user.save()
    return user

def login(email: str, password: str) -> User:
    user = User.objects(email=email).first()
    if user:
        if check_password(password, user.password):
            return user
        else:
            return None
    else:
        return None
    
def get_tocken(user: User) -> str:
    return get_hashed_password(user.email)

def update_user(name: str, surname: str, login: str) -> User:
    user = User.objects(login=login).first()
    if user:
        user.name = name
        user.surname = surname
        user.save()
        return user
    else:
        return None
    

def create_shop(title: str, user: User) -> Shop:
    slug = slugify(title)
    while Shop.objects(slug=slug).first():
        slug += "1"
    
    shop = Shop(title=title, owner=user, admins=[], slug=slug, is_active=True)
    shop.save()
    return shop


def get_shop(slug: str) -> Shop:
    return Shop.objects(slug=slug).first()

def get_shop_by_id(id: str) -> Shop:
    return Shop.objects(pk=id).first()

def get_users_shops(user: User) -> list:
    shops = Shop.objects(Q(admins__contains=user) | Q(owner=user))
    
    return list(shops)

def add_admin_to_shop(shop_slug: str, user_email: str):
    shop = Shop.objects(slug=shop_slug).first()
    user = User.objects(email=user_email).first()
    
    shop.admins.append(user)
    
    shop.save()    


def create_product(title: str, category: str, price: float, slug: str, coef: float, shop: Shop) -> Product:    
    product = Product(title=title, category=category, price=price, slug=slug, coef=coef, shop=shop)
    product.save()
    return product

def get_product(slug: str) -> Product:
    return Product.objects(slug=slug).first()

def get_product_by_id(id: str) -> Product:
    return Product.objects(pk=id).first()

def get_products_by_shop(shop: Shop) -> list:
    return list(Product.objects(shop=shop))

def update_product(title: str, category: str, price: float, slug: str, coef: float) -> Product:
    product = Product.objects(slug=slug).first()
    if product:
        product.title = title
        product.category = category
        product.price = price
        product.coef = coef
        product.save()
        return product
    else:
        return None
    
def delete_product(slug: str):
    product = Product.objects(slug=slug).first()
    product.delete()


def params_pars(params: str) -> dict:
    return json.loads(params)

def create_item(product: Product, parms_cnt: int, params: list) -> Item:
    item = Item(product=product, parms_cnt=parms_cnt)
    if parms_cnt == 1:
        item.a = params[0]
    elif parms_cnt == 2:
        item.a = params[0]
        item.b = params[1]
    item.save()
    return item

def get_item_by_id(id: str) -> Item:
    return Item.objects(pk=id).first()

def get_items_by_product(product: Product) -> list:
    return list(Item.objects(product=product))

def update_item(parms_cnt: int, params: list, id: str) -> Item:
    item = Item.objects(pk=id).first()
    if item:
        item.parms_cnt = parms_cnt
        if parms_cnt == 1:
            item.a = params[0]
        elif parms_cnt == 2:
            item.a = params[0]
            item.b = params[1]
        item.save()
        return item
    else:
        return None
    
def delete_item(id: str):
    item = Item.objects(pk=id).first()
    item.delete()


def products_pars(products: str) -> list:
    data = json.loads(products)
    prod_lst = []
    for el in data['products']:
        prd = get_product_by_id(el['product_id'])
        prod_lst.append(prd)
        
    return prod_lst


def create_template(title: str, shop: Shop, products: list) -> Template:    
    template = Template(title=title, shop=shop, products=products)
    template.save()
    return template

def get_template(slug: str) -> Template:
    return Template.objects(slug=slug).first()

def delete_template(id: str):
    template = Template.objects(pk=id).first()
    template.delete()

def get_template_by_id(id: str) -> Template:
    return Template.objects(pk=id).first()

def get_templates_by_shop(shop: Shop) -> list:
    return list(Template.objects(shop=shop))


def parce_items_response(items: str) -> list:
    # {cnt: 2, items: [{"item_id": "string", cnt: 2, a: "float", b: "float"}, {"item_id": "string", cnt: 1, a: "float"}]}
    data = json.loads(items)
    items = []
    for item in data["items"]:
        itm = Item.objects(pk=item["item_id"]).first()
        if int(item["cnt"]) == 2:
            items.append({"item": itm, "cnt": int(item["cnt"]), "a": float(item["a"]), "b": float(item["b"])})
        elif int(item["cnt"]) == 1:
            items.append({"item": itm, "cnt": int(item["cnt"]), "a": float(item["a"])})
        else:
            items.append({"item": itm, "cnt": int(item["cnt"])})

    return items

def modelsformat_to_response(items_str: str) -> dict:
    # {items: [{item: id, params_cnt: int, a: int, b: int}, ...]}
    data = json.loads(items_str)
    new_data = {}
    new_data['cnt'] = len(data['items'])
    new_data['items'] = []
    for el in data['items']:
        new_el = {
            'item_id': el['item'],
            'cnt': el['params_cnt'],
        }
        if el['params_cnt'] >= 1:
            new_el['a'] = el['a']
        if el['params_cnt'] == 2:
            new_el['b'] = el['b']
        new_data['items'].append(new_el)
    
    return new_data
        
def calculate_order_price(items: list) -> float:
    price = 0
    for item in items:
        col = 0
        if item["cnt"] == 2:
            col = item["a"] * item["b"]
        elif item["cnt"] == 1:
            col = item["a"]
        else:
            col = 1
        price += item["item"].product.price * col * item["item"].product.coef
        
    return price

def edit_on_order(items: list):
    for item in items:
        if item["cnt"] == 0:
            continue
        if item["cnt"] == 1:
            item["item"].a -= item["a"]
        if item["cnt"] == 2:
            item["item"].a -= item["a"]
            item["item"].b -= item["b"]
        item["item"].save()            

def create_order(shop: Shop, items: str) -> Order:
    order = Order(shop=shop)
    items_list = parce_items_response(items)
    order.price = calculate_order_price(items_list)
    items_data = {}
    items_data["items"] = []
    for itm in items_list:
        if itm["cnt"] == 2:
            items_data["items"].append({"item": str(itm["item"].id), "params_cnt": itm["cnt"], "a": itm["a"], "b": itm["b"]})
        elif itm["cnt"] == 1:
            items_data["items"].append({"item": str(itm["item"].id), "params_cnt": itm["cnt"], "a": itm["a"]})
        else:
            items_data["items"].append({"item": str(itm["item"].id), "params_cnt": itm["cnt"]})

    edit_on_order(items_list)

    order.items = str(items_data)
    order.created_at = datetime.datetime.now()
    order.save()
    
    return order

def order_price(shop: Shop, items: str) -> Order:
    items_list = parce_items_response(items)
    price = calculate_order_price(items_list)
    return price
    
def get_order_by_id(id: str) -> Order:
    return Order.objects(pk=id).first()

def delete_order(id: str):
    order = Order.objects(pk=id).first()
    order.delete()

def get_orders_by_shop(shop: Shop) -> list:
    return list(Order.objects(shop=shop).order_by('-created_at'))

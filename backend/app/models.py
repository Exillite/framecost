from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField, BooleanField, ReferenceField, URLField, DateTimeField, FloatField, DateField

import json

class User(Document):
    password = StringField(required=True)
    role = StringField(required=True)
    login = StringField(required=True)
    name = StringField(required=True)
    surname = StringField(required=True)
    email = StringField(required=True)
    is_active = BooleanField(default=True)
    
    def json_convert(self):
        return {
            "id": str(self.id),
            "login": self.login,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "role": self.role,
        }


class Shop(Document):
    title = StringField(required=True)
    owner = ReferenceField(User, required=True)
    admins = ListField(ReferenceField(User))
    slug = StringField(required=True)
    is_active = BooleanField(default=True)
    
    def json_convert(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "slug": self.slug,
            "owner": self.owner.json_convert(),
            "admins": [admin.json_convert() for admin in self.admins],
        }


class Product(Document):
    title = StringField(required=True)
    category = StringField(required=True)
    price = FloatField(required=True)
    slug = StringField(required=True)
    shop = ReferenceField(Shop, required=True)
    
    def json_convert(self):
        return {
            "id": str(self.pk),
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "slug": self.slug,
            "shop": self.shop.json_convert(),
        }


class Item(Document):
    product = ReferenceField(Product, required=True)
    parms_cnt = IntField(required=True) # 0 | 1 | 2
    a = FloatField()
    b = FloatField()
    
    def json_convert(self):
        params = {}
        if self.parms_cnt == 0:
            params = {"cnt": 0}
        if self.parms_cnt == 1:
            params = {"cnt": 1, "a": self.a}
        if self.parms_cnt == 2:
            params = {"cnt": 2, "a": self.a, "b": self.b}
        return {
            "id": str(self.pk),
            "product_id": self.product,
            "params": params,
        }


class Template(Document):
    title = StringField(required=True)
    shop = ReferenceField(Shop, required=True)
    products = ListField(ReferenceField(Product))

    def json_convert(self):
        return {
            "id": str(self.pk),
            "title": self.title,
            "shop": self.shop.json_convert(),
            "products": [products.json_convert() for products in self.products],
        }


class Order(Document):
    shop = ReferenceField(Shop, required=True)
    items = StringField(required=True) # JSON {items: [{item: id, params_cnt: int, a: int, b: int}, ...]}
    price = FloatField(required=True)
    created_at = DateTimeField(required=True)
    
    def json_convert(self):
        self.items = self.items.replace("\'", "\"")
        data = json.loads(self.items)
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
            
            item = Item.objects(pk=new_el["item_id"]).first()
            new_el["product"] = item.product.json_convert()
            new_data['items'].append(new_el)

        return {
            "id": str(self.pk),
            "shop_id": str(self.shop.id),
            "price": self.price,
            "products": new_data,
            "created_at": str(self.created_at),
        }

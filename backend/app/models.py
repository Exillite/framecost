from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField, BooleanField, ReferenceField, URLField, DateTimeField, FloatField, DateField

import crud

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
            "id": str(self.id),
            "category": self.category,
            "price": self.price,
            "slug": self.slug,
            "shop_id": self.shop.pk,
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
            "product_id": self.product.pk,
            "params": str(params),
        }


class Template(Document):
    title = StringField(required=True)
    shop = ReferenceField(Shop, required=True)
    products = ListField(ReferenceField(Product))

    def json_convert(self):
        return {
            "id": str(self.pk),
            "title": self.title,
            "shop_id": self.shop.pk,
            "products": [products.json_convert() for products in self.products],
        }


class Order(Document):
    shop = ReferenceField(Shop, required=True)
    items = StringField(required=True) # JSON {items: [{item: id, params_cnt: int, a: int, b: int}, ...]}
    price = FloatField(required=True)
    created_at = DateTimeField(required=True)
    
    def json_convert(self):
        return {
            "id": str(self.pk),
            "shop_id": str(self.shop.id),
            "price": self.price,
            "products": str(crud.modelsformat_to_response(self.items)),
            "created_at": str(self.created_at),
        }

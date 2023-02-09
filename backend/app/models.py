from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField, BooleanField, ReferenceField, URLField, DateTimeField, FloatField, DateField


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


class Product(Document):
    title = StringField(required=True)
    category = StringField(required=True)
    price = FloatField(required=True)
    slug = StringField(required=True)
    shop = ReferenceField(Shop, required=True)


class Item(Document):
    product = ReferenceField(Product, required=True)
    parms_cnt = IntField(required=True) # 0 | 1 | 2
    a = FloatField()
    b = FloatField()


class Template(Document):
    title = StringField(required=True)
    shop = ReferenceField(Shop, required=True)
    products = ListField(ReferenceField(Product))
    slug = StringField(required=True)
    

class Order(Document):
    shop = ReferenceField(Shop, required=True)
    products = StringField(required=True) # JSON {products: [{product: id, params: int, [a: int, b: int]}, ...]}
    price = FloatField(required=True)
    slug = StringField(required=True)
    created_at = DateTimeField(required=True)

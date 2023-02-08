from mongoengine import Document
from mongoengine.fields import StringField, IntField, ListField, BooleanField, ReferenceField, URLField, DateTimeField, FloatField, DateField


class User(Document):
    password = StringField(required=True)
    role = StringField(required=True)
    name = StringField(required=True)
    surname = StringField(required=True)
    email = StringField(required=True)
    is_active = BooleanField(default=True)


class Shop(Document):
    title = StringField(required=True)
    owner = ReferenceField(User, required=True)
    admins = ListField(ReferenceField(User))
    is_active = BooleanField(default=True)


class Product(Document):
    title = StringField(required=True)
    category = StringField(required=True)
    price = FloatField(required=True)
    shop = ReferenceField(Shop, required=True)


class Item(Document):
    product = ReferenceField(Product, required=True)
    shop = ReferenceField(Shop, required=True)
    parms_cnt = IntField(required=True) # 0 | 1 | 2
    a = FloatField()
    b = FloatField()


class Template(Document):
    title = StringField(required=True)
    shop = ReferenceField(Shop, required=True)
    producsts = ListField(ReferenceField(Product))
    
from enum import unique
from os import name
from mongoengine import Document, EmbeddedDocument
from mongoengine.document import DynamicDocument
from mongoengine.fields import (
    DictField,
    ListField,
    StringField,
    IntField,
    EmbeddedDocumentField,
)

class Users(EmbeddedDocument):
    name=StringField()
    email=StringField()
    phone=StringField()

class Websites(Document):
    name=StringField(max_length=120, primary_key=True)
    users=ListField(EmbeddedDocumentField(Users))
    productFields=ListField(StringField(max_length=120))

class ScrapingSites(Document):
    name=StringField(max_length=120, primary_key=True)

class Shipping(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class SkuItems(EmbeddedDocument):
    itemTitle=StringField(max_length=120)
    itemSalePrice=StringField(max_length=120)
    itemPrice=StringField(max_length=120)
    itemImgUrl=StringField()

class WebsiteProducts(EmbeddedDocument):
    title=StringField()
    pic=StringField()
    price=StringField(max_length=120)
    category=ListField(StringField(max_length=30))  
    name=StringField(max_length=120)
    type=StringField(max_length=120)
    regular_price=IntField(max_length=120)
    description=StringField()
    short_description=StringField()
    extraFields=DictField()

class KpopheartProducts(EmbeddedDocument):
    team=StringField(max_length=120)
    title=StringField()
    pic=StringField()
    price=StringField(max_length=120)
    category=ListField(StringField(max_length=30))


class EcommProduct(Document):
    skuID=StringField(max_length=120, required=True)
    ecomm=StringField(required=True)
    title=StringField(required=True)
    reviewCount=StringField(max_length=120)
    orders=StringField(max_length=120)
    rating=StringField(max_length=120)
    website=StringField(required=True)
    shipping=ListField(EmbeddedDocumentField(Shipping))
    skuItems=ListField(EmbeddedDocumentField(SkuItems))
    websiteProducts=ListField(EmbeddedDocumentField(WebsiteProducts))


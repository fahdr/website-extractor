from enum import unique
from os import name
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
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
    name=StringField(max_length=120)
    type=StringField(max_length=120)
    regular_price=IntField(max_length=120)
    description=StringField()
    short_description=StringField()
    categories=ListField(StringField(max_length=30))
    images=ListField(StringField(max_length=30))
    meta = {'allow_inheritance': True}

class KpopheartProducts(EmbeddedDocument):
    team=StringField(max_length=120)
    title=StringField()
    pic=StringField()
    price=StringField(max_length=120)
    category=ListField(StringField(max_length=30))


class AliExProduct(Document):
    skuID=IntField(max_length=120, required=True, primary_key=True)
    title=StringField(required=True)
    reviewCount=StringField(max_length=120)
    orders=StringField(max_length=120)
    rating=StringField(max_length=120)
    website=StringField(required=True)
    shipping=ListField(EmbeddedDocumentField(Shipping))
    skuItems=ListField(EmbeddedDocumentField(SkuItems))
    websiteProducts=ListField(EmbeddedDocumentField(KpopheartProducts))
    
class DraftAliExProduct(Document):
    skuID=IntField(max_length=120, required=True, primary_key=True)
    title=StringField(required=True)
    reviewCount=StringField(max_length=120)
    orders=StringField(max_length=120)
    rating=StringField(max_length=120)
    shipping=ListField(EmbeddedDocumentField(Shipping))
    skuItems=ListField(EmbeddedDocumentField(SkuItems))
    websiteProducts=ListField(EmbeddedDocumentField(KpopheartProducts))

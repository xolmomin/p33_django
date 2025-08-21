from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, CASCADE, ImageField

from apps.models.base import SlugBasedModel


class Category(SlugBasedModel):
    name = CharField(max_length=255)
    image = ImageField(upload_to='category/%Y/%m/%d')


class Product(SlugBasedModel):
    name = CharField(max_length=255)
    price = FloatField()
    description = TextField()
    category = ForeignKey('apps.Category', CASCADE)


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE)
    image = ImageField(upload_to='product/%Y/%m/%d')


class Comment(Model):
    product = ForeignKey('apps.Product', CASCADE)
    user = ForeignKey('auth.User', CASCADE)
    comment = CharField(max_length=255)

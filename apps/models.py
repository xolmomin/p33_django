from django.contrib.auth.models import User
from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, CASCADE, ImageField, SlugField, \
    DateTimeField
from django.utils.text import slugify


class SlugBasedModel(Model):
    slug = SlugField(unique=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)


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


class BlogCategory(Model):
    name = CharField(max_length=255)


class Blog(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('apps.BlogCategory', CASCADE)
    created_by = ForeignKey('auth.User', CASCADE, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

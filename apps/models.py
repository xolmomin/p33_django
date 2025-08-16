from django.contrib.auth.models import User
from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, CASCADE, ImageField, SlugField, \
    DateTimeField, BooleanField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


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

    @property
    def blog_count(self):
        return self.blogs.filter(archived=False).count()

    def __str__(self):
        return self.name


class Blog(Model):
    title = CharField(max_length=255)
    description = CKEditor5Field()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('apps.BlogCategory', CASCADE, related_name='blogs')
    archived = BooleanField(db_default=False)
    created_by = ForeignKey('auth.User', CASCADE, editable=False)
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

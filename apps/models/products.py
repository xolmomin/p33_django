from django.db.models import CharField, FloatField, TextField, ImageField, ForeignKey, CASCADE

from apps.models.base import UUIDBaseModel, CreatedBaseModel


class Product(UUIDBaseModel, CreatedBaseModel):
    name = CharField(max_length=255)
    price = FloatField()
    discount_price = FloatField(blank=True, null=True)
    description = TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def image_count(self):
        return self.images.count()

    @property
    def first_image(self):
        image = self.images.first()
        if image:
            return image.image.url
        return None


class ProductImage(UUIDBaseModel):
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
    image = ImageField(upload_to='images/%Y/%m/%d')

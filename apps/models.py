from django.db.models import Model, CharField, FloatField, TextField, ForeignKey, CASCADE, BigIntegerField, BinaryField, \
    BooleanField, DateField, DateTimeField, DecimalField, DurationField, EmailField, FileField, FilePathField, \
    GeneratedField, GenericIPAddressField, ImageField, IntegerField, JSONField, PositiveIntegerField, \
    PositiveBigIntegerField, PositiveSmallIntegerField, TimeField, URLField, UUIDField, TextChoices, SlugField
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    image = ImageField(upload_to='category/%Y/%m/%d')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = FloatField()
    description = TextField(max_length=255)
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name

#
# class Group(Model):
#     MEDIA_CHOICES = [
#         (
#             "Audio",
#             (
#                 ("vinyl", "Vinyl"),
#                 ("cd", "CD"),
#             ),
#         ),
#         (
#             "Video",
#             (
#                 ("vhs", "VHS Tape"),
#                 ("dvd", "DVD"),
#             ),
#         ),
#         ("unknown", "Unknown"),
#     ]
#
#     # class Type(TextChoices):
#     #     VIP = 'vip', 'VIP'
#     #     STANDARD = 'standard', 'Standard'
#
#     type = CharField(choices=MEDIA_CHOICES, max_length=20, blank=True)
#     bigintfield = BigIntegerField(null=True, blank=True)
#     binaryfield = BinaryField(null=True, blank=True)
#     booleanfield = BooleanField(null=True, blank=True)
#     charfield = CharField(max_length=255)
#     datefield = DateField(null=True, blank=True)
#     datetimefield = DateTimeField(null=True, blank=True)
#     decimalfield = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     durationfield = DurationField(null=True, blank=True)
#     emailfield = EmailField(null=True, blank=True)
#     filefield = FileField(null=True, blank=True)
#     # filepathfield = FilePathField(null=True, blank=True)
#     floatfield = FloatField(null=True, blank=True)
#     # generatedfield = GeneratedField(expression=) # TODO
#     genericipfield = GenericIPAddressField(null=True, blank=True)
#     imagefield = ImageField(null=True, blank=True)
#
#     integerfield = IntegerField(null=True, blank=True)
#     jsonfield = JSONField(null=True, blank=True)
#     positivebigintegerfield = PositiveBigIntegerField(null=True, blank=True)
#     positiveintegerfield = PositiveIntegerField(null=True, blank=True)
#     positivesmallintegerfield = PositiveSmallIntegerField(null=True, blank=True)
#     textfield = TextField(null=True, blank=True)
#     timefield = TimeField(null=True, blank=True)
#     urlfield = URLField(null=True, blank=True)
#     uuidfield = UUIDField(null=True, blank=True)
#     slugfield = SlugField(null=True, blank=True, editable=False)
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         self.slugfield = slugify(self.charfield)
#         super().save(force_insert, force_update, using, update_fields)
#
#
# """
# id (pk)
# slug
# uuid
#
# Apple iPhone 15 Pro Max
#
# https://daryo.uz/category/uzbekistan/wym0qx53kfkm
# https://daryo.uz/category/uzbekistan/45546546546
# https://olcha.uz/ru/product/view/apple-iphone-15-pro-max
# https://app.pdp.uz/academic/academic/time-table/2eadad21-11f1-4bd6-8234-53f88557e395/552ed03e-223a-4077-9d28-a3773addcb6b
# https://uzum.uz/uz/product/idish-yuvish-uchun-vosita-fairy-limon-3892?skuId=4917
# https://kun.uz/en/news/2025/02/26/uzbekistan-and-pakistan-establish-a-high-council-for-strategic-cooperation-set-2-billion-trade-target
#
# """

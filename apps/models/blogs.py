from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField, BooleanField
from django.db.models.fields import IntegerField
from django.db.models.fields.files import ImageFieldFile
from django_ckeditor_5.fields import CKEditor5Field

from apps.models.base import CreatedBaseModel


class BlogCategory(Model):
    name = CharField(max_length=255)

    @property
    def blog_count(self):
        return self.blogs.filter(archived=False).count()

    def __str__(self):
        return self.name


def image_validator(image: ImageFieldFile):
    image_mb = image.size / 1024 / 1024  # mb
    if not (image_mb <= 5):
        raise ValidationError("hajmi 5MB dan katta bo'lmasligi kerak")

    is_valid_extension = image.file.content_type in ('image/jpg', 'image/png')
    if not is_valid_extension:
        raise ValidationError("Formati png va jpg bo'lishi kerak")


class Blog(CreatedBaseModel):
    title = CharField(max_length=255)
    description = CKEditor5Field()
    image = ImageField(upload_to='blogs/%Y/%m/%d', validators=[image_validator])
    is_premium = BooleanField(db_default=False)
    price = IntegerField(db_default=1500)
    category = ForeignKey('apps.BlogCategory', CASCADE, related_name='blogs')
    archived = BooleanField(db_default=False)
    created_by = ForeignKey('auth.User', CASCADE, editable=False)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        return super().delete(using, keep_parents)

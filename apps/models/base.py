from django.db.models import Model, SlugField
from django.db.models.fields import DateTimeField
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


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

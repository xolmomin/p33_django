from django.contrib import admin

from apps.models import ProductImage, Product


class ProductStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    min_num = 0
    max_num = 8


@admin.register(ProductImage)
class ProductImageModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'image_count'
    inlines = [ProductStackedInline]

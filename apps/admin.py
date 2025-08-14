from django.contrib import admin

from apps.models import Blog, BlogCategory


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(BlogCategory)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

from django.contrib import admin

from apps.models import Blog, BlogCategory


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'archived'
    search_fields = 'title',

    actions = ['archived_to_unarchived_action']

    @admin.action(description="Arxivga o'tkazish")
    def archived_to_unarchived_action(self, request, queryset):
        queryset.update(archived=True)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(BlogCategory)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'archived_blogs', 'un_archived_blogs']

    actions = ['archived_to_unarchived_action', 'unarchived_to_archived_action']

    @admin.action(description="Arxivga o'tkazish")
    def archived_to_unarchived_action(self, request, queryset):
        for category in queryset:
            category.blogs.update(archived=True)

    @admin.action(description="Arxivdan chiqarish")
    def unarchived_to_archived_action(self, request, queryset):
        for category in queryset:
            category.blogs.update(archived=False)

    @admin.display(description='Arxivlanganlar soni')
    def archived_blogs(self, obj: BlogCategory):
        return obj.blogs.filter(archived=True).count()

    @admin.display(description='Arxivlanmaganlar soni')
    def un_archived_blogs(self, obj: BlogCategory):
        return obj.blogs.filter(archived=False).count()

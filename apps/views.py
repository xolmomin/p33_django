from django.views.generic import TemplateView, ListView, DetailView

from apps.models import Blog, Category, BlogCategory


class BlogListView(ListView):
    queryset = Blog.objects.filter(archived=False)
    template_name = 'apps/blogs/blog.html'
    context_object_name = 'blogs'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.GET.get('category')

        if category_id:
            qs = qs.filter(category_id=category_id)

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['latest_blogs'] = Blog.objects.order_by('-created_at')[:5]
        return context


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'apps/blogs/blog-detail.html'
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['latest_blogs'] = Blog.objects.order_by('-created_at')[:5]
        return context

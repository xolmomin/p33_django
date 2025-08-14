from django.views.generic import TemplateView, ListView, DetailView

from apps.models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'apps/blogs/blog.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'apps/blogs/blog-detail.html'
    context_object_name = 'blog'

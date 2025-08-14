from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from apps.models import Product, Category


class ProductListView(ListView):
    template_name = 'apps/product-list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'apps/product-detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'


class MainView(TemplateView):
    template_name = 'apps/main.html'


class BlogListView(TemplateView):
    template_name = 'apps/blogs/blog.html'

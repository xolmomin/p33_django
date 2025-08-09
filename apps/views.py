from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.models import Product, Category


class ProductListView(ListView):
    template_name = 'apps/product-list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context

from django.views.generic import ListView, DetailView

from apps.models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/products/product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/products/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.all()[:3]
        return context

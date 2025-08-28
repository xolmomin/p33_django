from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from apps.forms import CustomUserCreationForm
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


class RegisterCreateView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('product_list_view')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # send_email()
        return super().form_valid(form)


class LoginTemplateView(TemplateView):
    template_name = 'apps/auth/login.html'

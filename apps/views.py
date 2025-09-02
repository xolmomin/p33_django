from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from apps.forms import CustomUserCreationForm
from apps.models import Product, User
from apps.tasks import send_email


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

    def form_valid(self, form):
        _form = super().form_valid(form)
        # send_email(form.instance.email)  # 2-3sekund
        send_email.delay(form.instance.email)  # 0sekund
        return _form


class LoginTemplateView(LoginView):
    template_name = 'apps/auth/login.html'
    next_page = reverse_lazy('product_list_view')


class LogoutPageView(View):
    success_url = reverse_lazy('product_list_view')

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.success_url)


class UserProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/auth/profile.html'

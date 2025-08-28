from django.urls import path

from apps.views import ProductListView, RegisterTemplateView, LoginTemplateView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('register', RegisterTemplateView.as_view(), name='register_view'),
    path('login', LoginTemplateView.as_view(), name='login_view'),
    path('product/<uuid:pk>', ProductDetailView.as_view(), name='product_detail_view'),
]


"""
http://127.0.0.1:8000/register
http://localhost:8000/

"""
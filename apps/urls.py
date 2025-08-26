from django.urls import path

from apps.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/<uuid:pk>', ProductDetailView.as_view(), name='product_detail_view'),
]

# p33_django_db
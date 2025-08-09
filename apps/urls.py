from django.urls import path, include
from apps.views import ProductListView, ProductDetailView, MainView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/view/<slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('main', MainView.as_view(), name='main_view')
]

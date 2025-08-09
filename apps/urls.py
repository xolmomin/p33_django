from django.urls import path, include
from apps.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view')
]

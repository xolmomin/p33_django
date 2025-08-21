from django.urls import path

from apps.views import BlogListView, BlogDetailView, RegisterTemplateView, LoginTemplateView, ProductDetailView, \
    ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/detail', ProductDetailView.as_view(), name='product_detail_view'),
    path('login', LoginTemplateView.as_view(), name='login_view'),
    path('register', RegisterTemplateView.as_view(), name='register_view'),
    path('blogs', BlogListView.as_view(), name='blog_list_view'),
    path('blogs/<pk>', BlogDetailView.as_view(), name='blog_detail_view'),
]

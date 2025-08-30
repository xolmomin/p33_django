from django.urls import path

from apps.views import ProductListView, RegisterCreateView, LoginTemplateView, ProductDetailView, LogoutPageView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('register', RegisterCreateView.as_view(), name='register_view'),
    path('login', LoginTemplateView.as_view(), name='login_view'),
    path('logout', LogoutPageView.as_view(), name='logout_page_view'),
    path('product/<uuid:pk>', ProductDetailView.as_view(), name='product_detail_view'),
]

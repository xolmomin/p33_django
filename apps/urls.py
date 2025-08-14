from django.urls import path

from apps.views import BlogListView, BlogDetailView

urlpatterns = [
    path('blogs', BlogListView.as_view(), name='blog_list_view'),
    path('blogs/<pk>', BlogDetailView.as_view(), name='blog_detail_view'),
]

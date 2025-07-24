from django.urls import path

from .views import (BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView,
                    BlogPostListView, BlogPostUpdateView)

app_name = 'blog'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('post/edit/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('post/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]

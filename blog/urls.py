from django.urls import path

from .views import PostListView, PostDetailView, ContactView, AboutView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]
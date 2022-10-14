from django.urls import path, include

from . import views




urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('profile/', views.ProfilePostListView.as_view(), name='profile'),
    path('create-post/', views.CreatePost.as_view(), name='create-post'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    
]
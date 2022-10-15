from django.urls import path

from . import views




urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('profile/', views.ProfilePostListView.as_view(), name='profile'),
    path('create/', views.CreatePost.as_view(), name='create-post'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
    path('update/<int:pk>/', views.UpdatePost.as_view(), name='update-post'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    
]
from django.urls import path

from .views import PostListView, PostDetailView, SearchResultsView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]

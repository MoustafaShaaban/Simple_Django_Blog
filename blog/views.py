from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'posts'
    


    def get_queryset(self):
        query = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )    
        return posts

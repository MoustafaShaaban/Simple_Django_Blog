from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

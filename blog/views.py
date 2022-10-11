from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutView(TemplateView):
    template_name = 'about.html'



class ContactView(TemplateView):
    template_name = 'contact.html'
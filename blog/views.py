from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4


class ProfilePostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePost(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'posts/update_post.html'
    success_url = reverse_lazy('post-list')


class DeletePost(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'posts/delete_post.html'
	success_url = reverse_lazy('post-list')


class AboutView(TemplateView):
    template_name = 'about.html'



class ContactView(TemplateView):
    template_name = 'contact.html'
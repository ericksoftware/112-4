from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ["title", "subtitle", "body", "author", "status"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


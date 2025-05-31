from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.urls import reverse_lazy

class PostUpdateView(UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ["title", "subtitle", "body", "author"]

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy("post_list")

class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ["title", "subtitle", "body", "author"]
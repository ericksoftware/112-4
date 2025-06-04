from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Status  
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Published = Status.objects.get(name="Published")
        context['title'] = 'Published'
        context['post_list'] = (
            Post.objects
            .filter(status=Published)
            .order_by('-created_on')
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/drafts.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Draft = Status.objects.get(name="Draft")
        context['title'] = 'Draft'
        context['post_list'] = (
            Post.objects
            .filter(status=Draft)
            .filter(author=self.request.user)
            .order_by('created_on').reverse()
            )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/archived.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Archived = Status.objects.get(name="Archived")
        context['title'] = 'Archived'
        context['post_list'] = (
            Post.objects
            .filter(status=Archived)
            .filter(author=self.request.user)
            .order_by('created_on').reverse()
            )
        return context

class PostDetailView(UserPassesTestMixin , DetailView):
    template_name = 'posts/post_detail.html'
    model = Post

    def test_func(self):
        post = self.get_object()
        if post.status.name == "Published":
            return True
        elif post.status.name == "Draft" and self.request.user == post.author:  
            return True
        elif post.status.name == "Archived" and self.request.user.is_authenticated:
            return True
        return False

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


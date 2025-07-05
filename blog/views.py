from audioop import reverse

from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from django import forms


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = '/blog/'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blog_posts'
    success_url = '/blog/'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blog_post'
    success_url = '/blog/'

    def get(self, request, *args, **kwargs):
        blog_post = self.get_object()
        blog_post.increment_view_count()  # Увеличиваем количество просмотров
        return super().get(request, *args, **kwargs)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = '/blog/'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')


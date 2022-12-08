from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post, Tag
from .forms import CommentForm

# import my_site_1.dummy_data as dummy_data


def helpers(a):
    return a['date']
    
def helpers_db(a):
    return a.date



class IndexView(ListView):
    template_name = "blog_1/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"       # Since we are using "ListView", we can access "object_list" (by default) will send data to index.html

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog_1/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"



class PostDetailView(DetailView):
    template_name = "blog_1/post-detail.html"
    model = Post            # With subclass DetailView, Django will automatically search by primary key or slug(which we are using here in urls.py)
    context_object_name = "single_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context




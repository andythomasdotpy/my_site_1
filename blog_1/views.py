from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post, Tag

# import my_site_1.dummy_data as dummy_data


def helpers(a):
    return a['date']
    
def helpers_db(a):
    return a.date



# Create your views here.

# def starting_page(request):
#     my_posts_db = Post.objects.all().order_by("-date")[:3]

#     return render(request, "blog_1/index.html",
#     {
#         "posts_db": my_posts_db
#     })

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



# def posts(request):
#     # my_posts = dummy_data.posts
#     my_posts_db = Post.objects.all().order_by('-date')
#     # sorted_list = sorted(my_posts, key=helpers, reverse=True)
#     # sorted_list_db = sorted(my_posts_db, key=helpers_db) 

#     return render(request, "blog_1/all-posts.html",
#     {
#         "all_posts": my_posts_db
#     })


class PostDetailView(DetailView):
    template_name = "blog_1/post-detail.html"
    model = Post            # With subclass DetailView, Django will automatically search by primary key or slug(which we are using here in urls.py)
    context_object_name = "single_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_tags"] = self.object.tags.all()
        return context

# def post_detail(request, slug):
#     # my_posts = dummy_data.posts
#     # my_posts_db = Post.objects.all()
#     # identified_post_db = Post.objects.get(slug=slug)
#     identified_post_db = get_object_or_404(Post, slug=slug)
#     print(identified_post_db.author, identified_post_db.date)
#     print(identified_post_db.tags.all())
#     # identified_post = next(item for item in my_posts if item["slug"] == slug)
#     # identified_post_db = next(item for item in my_posts_db if item.slug == slug)


#     return render(request, "blog_1/post-detail.html", 
#     {
#         # "single_post": identified_post,
#         "single_post": identified_post_db,
#         "tags": identified_post_db.tags.all()
#     })



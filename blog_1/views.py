from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic import DetailView, View
from django.http import HttpResponseRedirect

from .models import Post, Tag, Comment
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



# class PostDetailView(DetailView):
#     template_name = "blog_1/post-detail.html"
#     model = Post            # With subclass DetailView, Django will automatically search by primary key or slug(which we are using here in urls.py)
#     context_object_name = "single_post"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["get_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context


# Now we create manual view to create our own logic
class PostDetailView(View):
    def func_context(self, post):
        context = {
            "single_post": post,
            "get_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),     # in models.py we used related_name="comments" for post column
        }
        return context


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = self.func_context(post)
        return render(request, "blog_1/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)      # commit equals false will prevent saving to the database but will create a new model instance, since we have exclded post (in form) we need to link it to post before saving
            comment.post = post     # now we set comment post = post of the slug for which the view was reached in the end (see a few lines above)
            comment.save()   # now that we've attached post we can save to database

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = self.func_context(post)
        return render(request, "blog_1/post-detail.html", context)
    



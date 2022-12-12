from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic import  View
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post
from .forms import CommentForm

# Create your views here


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

# Now we create manual view to create our own logic
class PostDetailView(View):
    def func_context(self, post, comment_form):
        context = {
            "single_post": post,
            "get_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),     # in models.py we used related_name="comments" for post column
        }        
        return context

    def get(self, request, slug):
        comment_form = CommentForm()
        post = Post.objects.get(slug=slug)

        context = self.func_context(post, comment_form)
        print(len(context["comments"]))

        if len(context["comments"]) == 0:
            context["has_comments"] = False
        else:
            context["has_comments"] = True

        print(context["has_comments"])
        return render(request, "blog_1/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)      # commit equals false will prevent saving to the database but will create a new model instance, since we have exclded post (in form) we need to link it to post before saving
            comment.post = post     # now we set comment post = post of the slug for which the view was reached in the end (see a few lines above)
            comment.save()   # now that we've attached post we can save to database

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = self.func_context(post, comment_form)
        return render(request, "blog_1/post-detail.html", context)
    

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False

        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render (request, "blog_1/saved-posts.html", context)
            
        

    def post(self, request):
        stored_posts = request.session.get("stored_posts")    # get posts stored in session, could be none or could be list were loooking for
        
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:         # first we check if id we'ge going to add is already in stored posts
            stored_posts.append(post_id)     # we add post id to stored_posts but we must save it
        else:
            stored_posts.remove(post_id)    
            
        request.session["stored_posts"] = stored_posts  # here we either create key "stored_posts" (if it doesn't exist) or we've updated it with updated stored_posts

        return HttpResponseRedirect("/")


def delete_session(request):
    try:
        del request.session["stored_posts"]
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")
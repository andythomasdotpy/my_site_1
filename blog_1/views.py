from django.shortcuts import render, get_object_or_404
from .models import Post
# import my_site_1.dummy_data as dummy_data


def helpers(a):
    return a['date']
    
def helpers_db(a):
    return a.date


# Create your views here.

def starting_page(request):
    # my_posts = dummy_data.posts
    # print(my_posts)
    my_posts_db = Post.objects.all().order_by("-date")[:3]
    
    for post in my_posts_db:
        print(post.date)

    print("-------------------------")

    # sorted_list = sorted(my_posts, key=helpers)
    # sorted_list_db = sorted(my_posts_db, key=helpers_db)

    # latest_posts = sorted_list[-3:]
    # latest_posts_db = my_posts_db[-3:]
    # print(latest_posts_db)

    
    return render(request, "blog_1/index.html",
    {
        # "posts": latest_posts,
        "posts_db": my_posts_db
    })


def posts(request):
    # my_posts = dummy_data.posts
    my_posts_db = Post.objects.all().order_by('-date')
    # sorted_list = sorted(my_posts, key=helpers, reverse=True)
    # sorted_list_db = sorted(my_posts_db, key=helpers_db) 

    return render(request, "blog_1/all-posts.html",
    {
        "all_posts": my_posts_db
    })


def post_detail(request, slug):
    # my_posts = dummy_data.posts
    # my_posts_db = Post.objects.all()
    # identified_post_db = Post.objects.get(slug=slug)
    identified_post_db = get_object_or_404(Post, slug=slug)
    print(identified_post_db.author, identified_post_db.date)
    print(identified_post_db.tags.all())
    # identified_post = next(item for item in my_posts if item["slug"] == slug)
    # identified_post_db = next(item for item in my_posts_db if item.slug == slug)


    return render(request, "blog_1/post-detail.html", 
    {
        # "single_post": identified_post,
        "single_post": identified_post_db,
        "tags": identified_post_db.tags.all()
    })



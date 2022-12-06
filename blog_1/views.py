from django.shortcuts import render
import my_site_1.dummy_data as dummy_data


def helpers(a):
    return a['date']


# Create your views here.

def starting_page(request):
    my_posts = dummy_data.posts


    sorted_list = sorted(my_posts, key=helpers)

    latest_posts = sorted_list[-3:]

    
    return render(request, "blog_1/index.html",
    {
        "posts": latest_posts
    })


def posts(request):
    my_posts = dummy_data.posts
    sorted_list = sorted(my_posts, key=helpers, reverse=True)

    return render(request, "blog_1/all-posts.html",
    {
        "all_posts": sorted_list
    })


def post_detail(request, slug):
    my_posts = dummy_data.posts

    identified_post = next(item for item in my_posts if item["slug"] == slug)


    return render(request, "blog_1/post-detail.html", 
    {
        "single_post": identified_post
    })


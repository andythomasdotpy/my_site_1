from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="starting_page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), 
        name="post-detail-page"), #/posts/my-first-post   slug is search engine indentifier
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("delete/", views.delete_session),

]
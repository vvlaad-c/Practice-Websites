from django.urls import path
from . import views

# Url patterns list
urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>/", views.post_detail, name="post-detail"),
]

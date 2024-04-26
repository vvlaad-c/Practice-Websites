from django.urls import path
from . import views 

# Patterns list
urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail"),
]

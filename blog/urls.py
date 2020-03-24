from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog"),
    path('post', views.blog_posts, name="post"),
]
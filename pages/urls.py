from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('projects_index', views.projects, name="projects"),

]

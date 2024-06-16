from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newpage", views.newPage, name="newpage"),
    path("edit", views.edit, name="edit"),
]

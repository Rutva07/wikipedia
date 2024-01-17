from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("created", views.created, name="created"),
    path("save", views.save, name="save"),
    path("random", views.get_random, name="get_random"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("<str:name>", views.entry, name="entry"),
    path("wiki/<str:name>", views.wikiEntry, name="wikiEntry"),
]

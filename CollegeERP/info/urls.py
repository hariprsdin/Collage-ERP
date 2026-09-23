from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("search/", views.search, name="search"),
    path("upload/", views.upload, name="upload"),
    path("redirect/", views.unsafe_redirect, name="unsafe_redirect"),
    path("cmd/", views.admin_debug, name="admin_debug"),
    path("profile/<str:username>", views.profile, name="profile"),
]

from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("post_list/", PostView.as_view(), name="post_list"),
    path("post_list/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("post_list/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("post_list/<int:pk>/edit", PostUpdateView.as_view(), name="post_update"),
    path("register/", RegisterView.as_view(), name="register"),
]

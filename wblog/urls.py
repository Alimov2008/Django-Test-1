from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("post_list/", PostView.as_view(), name="post_list"),
    path("post_list/<int:pk>", PostDetailView.as_view(), name="post_detail_view"),
]

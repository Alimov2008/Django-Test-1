from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from .models import Post


class HomeView(TemplateView):
    template_name = "wblog/home.html"


class PostView(ListView):
    model = Post
    template_name = "wblog/post_view.html"
    context_object_name = "posts"

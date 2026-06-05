from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


class HomeView(TemplateView):
    template_name = "wblog/home.html"


class PostView(ListView):
    model = Post
    template_name = "wblog/post_view.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "wblog/post_detail_view.html"

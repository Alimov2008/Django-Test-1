from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

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


class PostCreateView(CreateView):
    model = Post
    template_name = "wblog/post_create_view.html"
    fields = ["title", "context"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create New Post"
        return context

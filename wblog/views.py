from django.db.models.query import QuerySet
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
        """
        in case of form being valid assigns post author to the user who created it
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create New Post"
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = "wblog/post_delete_view.html"
    success_url = reverse_lazy("post_list")

    def get_object(self, queryset: QuerySet[Any] | None = None) -> Model:
        """
        Disallows Post instance deletion in case
        of current user and post author mismatch
        """
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionError("Not your post")
        return obj

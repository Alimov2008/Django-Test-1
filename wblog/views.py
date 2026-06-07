from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "wblog/post_create_view.html"
    fields = ["title", "context"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
        In case of form being valid assigns post author to the user who created it
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Adds an additional attribute to context data being send to template
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create New Post"
        return context


class PostUpdateView(UpdateView):
    model = Post
    template_name = "wblog/post_update_view.html"
    fields = ["title", "context"]
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


class PostDeleteView(DeleteView):
    model = Post
    template_name = "wblog/post_delete_view.html"
    success_url = reverse_lazy("post_list")
    context_object_name = "post"

    def get_object(self, queryset: QuerySet[Any] | None = None) -> Model:
        """
        Disallows Post instance deletion in case
        of current user and post author mismatch
        """
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionError("Not your post")
        return obj


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

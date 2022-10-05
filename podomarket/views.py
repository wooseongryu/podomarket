from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from braces.views import LoginRequiredMixin
from allauth.account.views import PasswordChangeView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm


def index(request):
    return render(request, 'podomarket/index.html')

class IndexView(ListView):
    model = Post
    template_name = 'podomarket/index.html'
    context_object_name = 'posts'
    paginate_by = 8
    ordering = ["-dt_updated"]

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'podomarket/post_detail.html'
    pk_url_kwarg = 'post_id'

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'podomarket/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={"post_id": self.object.id})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'podomarket/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={"post_id": self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'podomarket/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('index')

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')


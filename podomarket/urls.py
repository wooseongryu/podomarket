from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'posts/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='post-detail',    
    ),
    path(
        'posts/new/',
        views.PostCreateView.as_view(),
        name='post-create',
    ),
    path(
        'posts/<post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='post-update',
    ),
    path(
        'posts/<post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='post-delete',
    ),
    path(
        'users/<int:user_id>/',
        views.ProfileView.as_view(),
        name='profile',
    )
]



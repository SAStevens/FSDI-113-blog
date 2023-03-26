from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostDelelteView,
    PostUpdateView,
    DraftPostListView
)


urlpatterns = [
    path("", PostListView.as_view(), name="posts/list"),
    path("drafts/", DraftPostListView.as_view(), name="draft/posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="posts/detail"),
    path("posts/new/", PostCreateView.as_view(), name="posts/new"),
    path("posts/int:pk>/edit/", PostUpdateView.as_view(), name="posts/edit"),
    path("posts/int:pk>/delete/", PostDelelteView.as_view(), name="posts/delete"),
]

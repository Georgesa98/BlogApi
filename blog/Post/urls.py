from django.urls import path, include

from .views import CreatePostView, RetrievePost

urlpatterns = [
    path("create/", CreatePostView.as_view()),
    path("<int:pk>", RetrievePost.as_view()),
    path("comment/", include("Post.Comment.urls")),
    path("like/", include("Post.Like.urls")),
]

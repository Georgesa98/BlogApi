from django.urls import path
from .views import CreateCommentView, RetrieveComment

urlpatterns = [
    path("create/", CreateCommentView.as_view()),
    path("<int:pk>", RetrieveComment.as_view()),
]

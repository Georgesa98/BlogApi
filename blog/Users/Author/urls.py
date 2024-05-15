from django.urls import path
from .views import AuthorView, RetrieveAuthorView

urlpatterns = [
    path("create/", AuthorView.as_view()),
    path("<int:pk>", RetrieveAuthorView.as_view()),
]

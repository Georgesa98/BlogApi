from django.urls import path
from .views import ReaderView, RetrieveReaderView

urlpatterns = [
    path("create/", ReaderView.as_view()),
    path("<int:pk>", RetrieveReaderView.as_view()),
]

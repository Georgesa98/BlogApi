from django.urls import path
from .views import DiscoverPosts, SearchPosts

urlpatterns = [
    path("", DiscoverPosts.as_view()),
    path("/search", SearchPosts.as_view()),
]

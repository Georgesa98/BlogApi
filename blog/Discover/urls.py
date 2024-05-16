from django.urls import path
from .views import DiscoverPosts, SearchPosts, Foryou

urlpatterns = [
    path("", DiscoverPosts.as_view()),
    path("/search", SearchPosts.as_view()),
    path("/foryou", Foryou.as_view()),
]

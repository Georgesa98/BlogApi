from django.urls import path

from .views import LikeView

urlpatterns = [path("create/", LikeView.as_view())]

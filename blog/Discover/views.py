from django.shortcuts import render
from rest_framework.views import APIView, Response, status
import random
from Post.serializer import GetPostSer
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from django.db.models import Q
from Post.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
def get_randomized_posts():
    cache_key = "random_posts"
    cached_data = cache.get(cache_key)
    if cached_data:
        seed, random_posts = cached_data
    else:
        seed = random.randint(1, 1000)
        now = timezone.now()
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0)

        all_posts = Post.objects.filter(
            created_at__gte=start_of_month, created_at__lte=now
        )
        random_posts = random.sample(list(all_posts), all_posts.count())
        cache.set(cache_key, (seed, random_posts), timeout=60)
    return seed, random_posts


def get_randomized_posts_foryou(tags):
    cache_key = "random_posts_foryou"
    cached_data = cache.get(cache_key)
    if cached_data:
        seed, random_posts = cached_data
    else:
        seed = random.randint(1, 1000)
        now = timezone.now()
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0)

        all_posts = Post.objects.filter(
            created_at__gte=start_of_month, created_at__lte=now, tags__in=tags.all()
        )
        random_posts = random.sample(list(all_posts), all_posts.count())
        cache.set(cache_key, (seed, random_posts), timeout=60)
    return seed, random_posts


class DiscoverPosts(APIView, PageNumberPagination):

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            seed, random_posts = get_randomized_posts()
            result = self.paginate_queryset(random_posts, request, view=self)
            posts_ser = GetPostSer(result, many=True)
            return Response({"page": page, "result": posts_ser.data})
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchPosts(APIView):
    def get(self, request):
        try:
            query = request.query_params.get("query")
            if not query:
                return Response({"error": 'missing parameter "query"'})
            elif len(query) < 3:
                return Response({"error": "please provide more details"})
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(title__icontains=query)
            )
            serializer = GetPostSer(results, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class Foryou(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            user_tags = request.user.recommendation
            seed, random_posts = get_randomized_posts_foryou(user_tags)
            result = self.paginate_queryset(random_posts, request, view=self)
            posts_ser = GetPostSer(result, many=True)
            return Response({"page": page, "result": posts_ser.data})
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

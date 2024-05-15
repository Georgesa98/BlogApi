from django.shortcuts import render
from rest_framework.views import APIView, Response, status
import random
from Post.serializer import GetPostSer
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from django.db.models import Q
from Post.models import Post


# Create your views here.
class DiscoverPosts(APIView, PageNumberPagination):
    def get_randomized_posts(self):
        cache_key = "random_posts"
        cached_data = cache.get(cache_key)
        if cached_data:
            seed, random_posts = cached_data
        else:
            seed = random.randint(1, 1000)
            all_posts = Post.objects.all()
            random_posts = random.sample(list(all_posts), all_posts.count())
            cache.set(cache_key, (seed, random_posts), timeout=60)
        return seed, random_posts

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            seed, random_posts = self.get_randomized_posts()
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

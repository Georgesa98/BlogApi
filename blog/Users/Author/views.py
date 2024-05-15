from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from .models import Author
from .serializers import CreateAuthorSer, GetAuthorSer, UpdateAuthorSer


# Create your views here.
class AuthorView(APIView):
    def post(self, request):
        try:
            serializer = CreateAuthorSer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            author = Author.objects.all()
            serializer = GetAuthorSer(author, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveAuthorView(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = GetAuthorSer(author, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = UpdateAuthorSer(instance=author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            author.save()
            return Response("deleted successfully", status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_404_NOT_FOUND)

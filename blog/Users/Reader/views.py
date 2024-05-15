from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from .models import Reader
from .serializers import CreateReaderSer, UpdateReaderSer, GetReaderSer


# Create your views here.
class ReaderView(APIView):
    def post(self, request):
        try:
            serializer = CreateReaderSer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            reader = Reader.objects.all()
            serializer = GetReaderSer(reader, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveReaderView(APIView):
    def get(self, request, pk):
        try:
            reader = Reader.objects.get(pk=pk)
            serializer = GetReaderSer(reader, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            reader = Reader.objects.get(pk=pk)
            serializer = UpdateReaderSer(instance=reader, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            reader = Reader.objects.get(pk=pk)
            reader.delete()
            reader.save()
            return Response("deleted successfully", status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_404_NOT_FOUND)

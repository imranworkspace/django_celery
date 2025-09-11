from django.core.cache import cache
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BookModel
from api.serializer import BookSerializer
from datetime import timedelta
import time

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60*5)

class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        start_cachetime=time.time() # start time
        key = "book_list"
        data = cache.get(key)

        if data:
            end_cachetime = time.time()     # record end time
            return Response({"source": "cache", "data": data,"cache_execution_time": f'{end_cachetime - start_cachetime:.6f} sec'})
        
        start_dbtime=time.time() # start time
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        data = serializer.data

        cache.set(key, data, CACHE_TTL)
        end_dbtime=time.time()
        return Response({"source": "db", "data": data,"cache_execution_time":f'{end_dbtime-start_dbtime:.6f} sec'})

    def retrieve(self, request, pk=None):
        start_cachetime=time.time() # start time
        key = f"book_{pk}"
        data = cache.get(key)

        if data:
            end_cachetime = time.time()     # record end time
            return Response({"source": "cache", "data": data,"cache_execution_time": f'{end_cachetime - start_cachetime:.6f} sec'})
        
        start_dbtime=time.time() # start time
        try:
            book = BookModel.objects.get(pk=pk)
        except BookModel.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        data = serializer.data

        cache.set(key, data, CACHE_TTL)
        end_dbtime=time.time()
        return Response({"source": "db", "data": data,"cache_execution_time":f'{end_dbtime-start_dbtime:.6f} sec'})

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete("book_list")  # invalidate list cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            book = BookModel.objects.get(pk=pk)
        except BookModel.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete("book_list")
            cache.delete(f"book_{pk}")  # invalidate detail cache
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            book = BookModel.objects.get(pk=pk)
        except BookModel.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        cache.delete("book_list")
        cache.delete(f"book_{pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)

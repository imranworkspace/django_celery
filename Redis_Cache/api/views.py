from django.core.cache import cache
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookModel
from api.serializer import BookSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60*5)

class BookListView(APIView):
    def get(self, request):
        key = "book_list"

        # Try cache first
        if cache.get(key):
            data = cache.get(key)
            return Response({"source": "cache", "data": data})

        # If not in cache, fetch from DB
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        data = serializer.data

        # Save to cache
        cache.set(key, data, timeout=CACHE_TTL)

        return Response({"source": "db", "data": data})

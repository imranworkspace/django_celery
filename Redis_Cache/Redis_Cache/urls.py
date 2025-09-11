from django.contrib import admin
from django.urls import path
from api.views import BookListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", BookListView.as_view(), name="book-list"),
]

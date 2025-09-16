from django.contrib import admin
from django.urls import path
from api.views import cel_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cel_view),
]

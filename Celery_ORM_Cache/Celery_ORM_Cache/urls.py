from django.contrib import admin
from django.urls import path
from myapp import views
from myapp2 import views as app2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('home2/',app2.index,name='home2'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('check_result/<str:task_id>',views.check_result,name='check_result'),
]

from django.shortcuts import render
from api.tasks import mul,visit_cache
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

def cel_view(request):
    visits = visit_cache.delay()
    print('task= ',visits)
    return JsonResponse({'resp':f'{visits}'},status=status.HTTP_200_OK)

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from rest_framework import viewsets


def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})
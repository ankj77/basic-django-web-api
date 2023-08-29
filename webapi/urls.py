
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from coupon.views import  hello_world



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fetch-coupon/', hello_world),

]

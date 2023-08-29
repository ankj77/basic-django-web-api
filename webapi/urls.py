
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from coupon.views import CouponViewSet

# Serializers define the API representation.

router = DefaultRouter()
router.register(r'tasks', CouponViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # path('api-auth/', include('rest_framework.urls.py', namespace='rest_framework'))

]

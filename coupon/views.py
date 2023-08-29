from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .models import Coupons
from .serializers import CouponSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupons.objects.all()
    serializer_class = CouponSerializer
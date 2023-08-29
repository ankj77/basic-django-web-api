from django.db import models

# Create your models here.

from django.db import models



from rest_framework import serializers
from .models import Coupons

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'


from django.contrib import admin
from django.urls import path, include

from coupon.views import  fetch_coupon



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fetch-coupon/', fetch_coupon),

]

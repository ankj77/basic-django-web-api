from django.db import models

# Create your models here.

from django.db import models


class Coupons(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.status

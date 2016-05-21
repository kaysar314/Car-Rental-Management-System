from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
# Create your models here.


class Offer(models.Model):
    car_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    daily_rental = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DurationField()

    def __str__(self):
        return '-'.join((self.owner.username, self.car_name, str(self.daily_rental)))

class Deal(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField('date published')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=20)
    drive_license = models.ImageField(null=True)
    social_identity = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    alipay = models.ImageField(null=True)



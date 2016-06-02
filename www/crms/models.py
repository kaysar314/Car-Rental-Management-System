# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

BRAND_CHOICES = (('丰田', '丰田'), ('大众', '大众'), ('本田', '本田'))
MODEL_CHOICES = {'大众': (('甲壳虫', '甲壳虫'), ('迈腾', '迈腾'), ('捷达', '捷达')),
                 '丰田': (('凯美瑞', '凯美瑞'), ('卡罗拉', '卡罗拉'), ('锐志', '锐志')),
                 '本田': (('雅阁', '雅阁'), ('飞度', '飞度'), ('凌派', '凌派')),
}

GEAR_BOX_CHOICES = (('Manual', 'Manual'), ('Automatic', 'Automatic'))

def get_model_choices():
    return MODEL_CHOICES['丰田']

def get_free_car_choices():
    return (('A', 'A'), ('B', 'B'), ('C', 'C'))

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, null=True)
    model = models.CharField(max_length=50, choices=get_model_choices(), null=True)
    gear_box = models.CharField(max_length=20, choices=GEAR_BOX_CHOICES, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='car')
    displacement = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.owner.username + " " + self.name


    def image_tag(self):
        return u'<img src="%s" />' % self.image.url

class Offer(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, null=True)
    daily_rental = models.PositiveIntegerField()
    fetch_date = models.DateTimeField('fetch date', null=True)
    return_date = models.DateTimeField('return date', null=True)

    def __str__(self):
        return '-'.join((self.car.name, str(self.daily_rental)))

class Deal(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fetch_date = models.DateTimeField('fetch date', null=True)
    return_date = models.DateTimeField('return date', null=True)
    is_accept = models.BooleanField(default=False)

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    realname = models.CharField(max_length=20, blank=True)
    drive_license = models.ImageField(null=True, blank=True)
    social_identity = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=20, blank=True)
    alipay = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (self.owner.username + "'s Profile")


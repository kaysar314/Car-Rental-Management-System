from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

BRAND_CHOICES = (('丰田', '丰田'), ('大众', '大众'), ('本田', '本田'))
MODEL_CHOICES = {'大众': (('甲壳虫', '甲壳虫'), ('迈腾', '迈腾'), ('捷达', '捷达')),
                 '丰田': (('凯美瑞', '凯美瑞'), ('卡罗拉', '卡罗拉'), ('锐志', '锐志')),
                 '本田': (('雅阁', '雅阁'), ('飞度', '飞度'), ('凌派', '凌派')),
}

def get_brand_choices(brand):
    return MODEL_CHOICES[brand]

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, null=True)
    model = models.CharField(max_length=50, choices=get_brand_choices(brand), null=True)
    manual = models.BooleanField()
    img = models.ImageField(null=True, blank=True)

    displacement = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.owner.username + " " + self.name




class Offer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    daily_rental = models.DecimalField(max_digits=5, decimal_places=2)
    fetch_date = models.DateTimeField('fetch date', null=True)
    return_date = models.DateTimeField('return date', null=True)

    def __str__(self):
        return '-'.join((self.car.name, str(self.daily_rental)))

class Deal(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, unique=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fetch_date = models.DateTimeField('fetch date', null=True)
    return_date = models.DateTimeField('return date', null=True)

    # def __str__(self):
    #     return '-'.join((self.offer.owner.username, self.tenant.username, self.offer.car.name, self.fetch_date, self.return_date))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    realname = models.CharField(max_length=20)
    drive_license = models.ImageField(null=True)
    social_identity = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    alipay = models.ImageField(null=True)



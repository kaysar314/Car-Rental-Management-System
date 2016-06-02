from rest_framework import serializers
from django.contrib.auth.models import User
from crms.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'profile')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        # fields = ('url', 'realname', 'drive_license', 'social_identity', 'phone', 'location', 'alipay')
        fields = '__all__'

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        # fields = ('url', 'owner', 'name', 'brand', 'model', 'gear_box', 'image', 'displacement', 'description')
        fields = '__all__'

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        # fields = ('url', 'car', 'daily_rental', 'fetch_date', 'return_date')
        fields = '__all__'

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        # fields = ('url', 'offer', 'tenant', 'fetch_date','return_date', 'is_accept')
        fields = '__all__'

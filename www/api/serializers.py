from rest_framework import serializers
from django.contrib.auth.models import User
from crms.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'realname', 'drive_license', 'social_identity', 'phone', 'location', 'alipay')
        # fields = '__all__'

class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer(required=False)
    image = serializers.ReadOnlyField(source='image.url')
    class Meta:
        model = Car
        fields = ('id', 'owner', 'name', 'brand', 'model', 'gear_box', 'image','displacement', 'description')
        # fields = '__all__'

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    car = CarSerializer(required=False)
    class Meta:
        model = Offer
        fields = ('id', 'car', 'daily_rental', 'fetch_date', 'return_date')
        # fields = '__all__'

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        fields = ('id', 'offer', 'tenant', 'fetch_date','return_date', 'is_accept')
        # fields = '__all__'

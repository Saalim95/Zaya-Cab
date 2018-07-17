from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class TripUserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Trip
        fields = ('commuter', 'source',)

class TripDriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('driver', 'source',)

class DriverSerializer(serializers.ModelSerializer):

    def update(self, obj, data):
        obj.status = data.get("status", obj.status)
        obj.save()
        return obj

    class Meta:
        model = Driver
        exclude = ('name', 'user',)


class TripSerialier(serializers.ModelSerializer):

    class Meta:
        model = Trip
        exclude = ('commuter', 'driver')


class UserLocationSerializer(serializers.ModelSerializer):

    def update(self, obj, data):
        obj.lat = data.get("lat", obj.lat)
        obj.long = data.get("long", obj.long)
        obj.save()
        return obj

    class Meta:
        model = Commuter
        fields = ('lat', 'long')

from rest_framework import serializers
from django.contrib.auth.models import User
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from backoffice.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

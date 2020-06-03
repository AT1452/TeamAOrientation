from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Donor
        fields = ('name', 'ticket')
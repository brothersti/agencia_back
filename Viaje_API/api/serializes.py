from django.core import serializers
from rest_framework import serializers

from .models import Bus

class BusWithoutChofer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields =['IdBus', 'NumeroBus']
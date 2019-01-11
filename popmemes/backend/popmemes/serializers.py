"""
Create serializers to convert model instances to JSON so that the frontend can
work with the received data easily.
"""

from rest_framework import serializers
from .models import Popmemes

class MemeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Popmemes
    fields = ('id', 'user')

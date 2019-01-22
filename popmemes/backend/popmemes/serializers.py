"""
Create serializers to convert model instances to JSON so that the frontend can
work with the received data easily.
"""

from rest_framework import serializers
from .models import PopImage

class MemeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PopImage
    fields = ('id', 'user', 'pop_img', 'freq')

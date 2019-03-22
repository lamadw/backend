from rest_framework import serializers

from .models import requestinstuctor,provedinstuctor
from django.contrib.auth.hashers import make_password
class requesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestinstuctor
        fields = '__all__'
class provedSerializer(serializers.ModelSerializer):
    class Meta:
        model = provedinstuctor
        fields = '__all__'

'''  def create(self, validated_data):
        validated_data['password1'] = make_password(validated_data.get('password1'))
        validated_data['password2'] = make_password(validated_data.get('password2'))
        return super(InstructureSerializer, self).create(validated_data)
'''


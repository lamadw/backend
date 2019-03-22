from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import userrule
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = userrule
        fields = '__all__'

   



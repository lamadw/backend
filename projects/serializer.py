from rest_framework import serializers
from.models import project,File
class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        read_only_fields =['user']


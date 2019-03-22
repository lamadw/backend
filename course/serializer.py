from rest_framework import serializers
from.models import course,courseinstructure,hwincourse,studentincourse
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'

class courseinstructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = courseinstructure
        fields = '__all__'

class hwincourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = hwincourse
        fields = '__all__'

class studentincourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentincourse
        fields = '__all__'
                       
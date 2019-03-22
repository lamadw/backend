from django.shortcuts import render
from student.serializers import StudentSerializer
from rest_framework import generics,mixins
from .models import userrule
from rest_framework import filters
class StudentListCreate(generics.ListCreateAPIView):
    queryset = userrule.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['userid__username']

class StudentRetrive(generics.RetrieveAPIView):
    queryset = userrule.objects.all()
    serializer_class = StudentSerializer

# Create your views here.

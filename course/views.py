from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from .models import course,studentincourse,hwincourse,courseinstructure
from rest_framework import filters
from rest_framework import generics,mixins
from rest_framework.response import Response
from .serializer import CourseSerializer,courseinstructureSerializer,hwincourseSerializer,studentincourseSerializer
class CourseListCreate(generics.ListCreateAPIView):
     queryset = course.objects.all()
     serializer_class  = CourseSerializer
     filter_backends = (filters.SearchFilter,)
     search_fields = ['=courseid']

  

class CourseUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = course.objects.all()
     serializer_class  = CourseSerializer

class courseinstructureListCreate(generics.ListCreateAPIView):
     queryset = courseinstructure.objects.all()
     serializer_class  = courseinstructureSerializer
     filter_backends = (filters.SearchFilter,)
     search_fields = ['=instructorname__username']

  

class courseinstructureUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = courseinstructure.objects.all()
     serializer_class  = courseinstructureSerializer
     
class studentincourseListCreate(generics.ListCreateAPIView):
     queryset = studentincourse.objects.all()
     serializer_class  = studentincourseSerializer
     filter_backends = (filters.SearchFilter,)
     search_fields = ['=courseid','=studentName__username']

  

class studentincourseUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = studentincourse.objects.all()
     serializer_class  = studentincourseSerializer
# Create your views here.
class hwincourseListCreate(generics.ListCreateAPIView):
     queryset = hwincourse.objects.all()
     serializer_class  = hwincourseSerializer
     filter_backends = (filters.SearchFilter,)
     search_fields = ['=courseid','=instructor__username']

  

class hwincourseSerializerUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = hwincourse.objects.all()
     serializer_class  =hwincourseSerializer
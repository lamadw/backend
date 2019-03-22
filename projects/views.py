from django.shortcuts import render
from rest_framework.views import APIView
from .models import project,File
from rest_framework import generics,mixins
from rest_framework.response import Response
from .serializer import projectSerializer,FileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class ProjectListCreate(generics.ListCreateAPIView):
     queryset = project.objects.all()
     serializer_class  = projectSerializer
  
# Create your views here.
''' authentication_classes=[]
    permission_classes =[]
    def post(self, request, format=None):
        qs = project.objects.all()
        serializer  = projectSerializer(qs,many=True)
        return Response(serializer.data)
        '''
class ProjectUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = project.objects.all()
     serializer_class  = projectSerializer
     authentication_classes= (SessionAuthentication, BasicAuthentication)
     permission_classes =  (IsAuthenticated,)

class FileListCreate(generics.ListCreateAPIView):
     queryset = File.objects.all()
     serializer_class  = FileSerializer

class FileUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView ):
     queryset = File.objects.all()
     serializer_class  = FileSerializer


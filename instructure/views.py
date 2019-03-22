from django.shortcuts import render

from instructure.serializer import requesteSerializer,provedSerializer
from rest_framework import generics,mixins
from.models import requestinstuctor,provedinstuctor
class InstructureListCreate(generics.ListCreateAPIView):
    queryset = requestinstuctor.objects.all()
    serializer_class =  requesteSerializer

class InstructureUpdteRetrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = requestinstuctor.objects.all()
    serializer_class =  requesteSerializer
  
class provedListCreate(generics.ListCreateAPIView):
    queryset = provedinstuctor.objects.all()
    serializer_class =  provedSerializer

class provedUpdteRetrive(generics.RetrieveUpdateAPIView):
    queryset = provedinstuctor.objects.all()
    serializer_class =  provedSerializer


    
  
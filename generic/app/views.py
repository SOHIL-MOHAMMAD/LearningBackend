from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import Student
from .serializer import StudentSerializer
# Create your views here.

class StudentList(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
class StudentListUpdate(generics.RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class  = StudentSerializer
  lookup_field = 'pk'


class List(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer



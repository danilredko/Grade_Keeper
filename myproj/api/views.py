from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from courses.models import Course
from .serializers import CourseSerializer

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

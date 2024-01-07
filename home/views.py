from django.shortcuts import render
from rest_framework import viewsets
from home.models import CourseMaster
from home.serializers import CourseSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseMaster.objects.all()
    serializer_class = CourseSerializer
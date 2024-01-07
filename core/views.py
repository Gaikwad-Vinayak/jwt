from django.shortcuts import render
from core.models import Student, Institute, Grade
from core.serializers import StudentSerializers, InstituteSerializers, CustomStudentSerializer, GradeSerializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from core.base_request import OpenBaseViewSet
from rest_framework.response import Response

# Create your views here.

class StudentViewSet(OpenBaseViewSet):
    
    def list(self, request):
        queryset = Student.objects.values('id','institute__name')
        serialized_data = CustomStudentSerializer(queryset, many=True).data
        return Response(serialized_data)
    

class InstituteViewSet(viewsets.ModelViewSet):
    queryset  = Institute.objects.all()
    serializer_class = InstituteSerializers


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.filter(title__iexact='Vinaya')
    serializer_class = GradeSerializers
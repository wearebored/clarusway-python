from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import student_serilazer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
def Student(req):
    return HttpResponse("ders5")


@api_view(["GET"]) #HANGİ METODLARIN KULLANILACAĞI YAZILIR
def home(req):
    return Response({
        "home":"homes"
    })


@api_view(["GET"])
def student_list(req):
    students = Students.objects.all()
    data=student_serilazer(students,many=True)
    return Response(data.data)


@api_view(["POST"])
def create(req):
    data=student_serilazer(data=req.data)
    if data.is_valid():
        data.save()
        message={
            "mesaj":"işlme başarılı"
        }
        return Response(message,status=status.HTTP_201_CREATED)
        
    return Response(data.errors)


@api_view(["GET"])
def details(req,pk):
    # student=Students.objects.get(id=pk)
    student=get_object_or_404(Students,id=pk)
    data=student_serilazer(student)
   
    return Response(data.data)


@api_view(["PUT"])
def putlama(req,pk):
    student=get_object_or_404(Students,id=pk)
    data=student_serilazer(student,data=req.data)
    if data.is_valid():
        data.save()
        message={
            "mesaj":"işlme başarılı"
        }
        return Response(message,status=status.HTTP_201_CREATED)
        
    return Response(data.errors)

@api_view(["DELETE"])
def silme(req,pk):
    student=get_object_or_404(Students,id=pk)
    student.delete()
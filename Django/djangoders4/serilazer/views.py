from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view



def serilazerlar(req):
    return HttpResponse("serilazers")


@api_view(["GET","POST"])
def student_api(req):
    pass


@api_view(["GET","PUT","DELETE","PATCH"])
def student_api_put(req,pk):
    pass
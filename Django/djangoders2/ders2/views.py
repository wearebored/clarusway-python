from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ders2(req):
    return HttpResponse("ders2")

def der3(req):
    return HttpResponse("der3")
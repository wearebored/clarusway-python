from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
dersler=["awe","adwa","waew"]
def ders2(req):
    
    return HttpResponse(dersler)
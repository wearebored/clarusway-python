from django.shortcuts import render
from django.http import HttpResponse
# ------------------
from .models import Student
# ------------------
# from rest_framework.generics import GenericAPIView,mixins
# from .serializers import student_seria
# ------------------
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import student_seria

# Create your views here.
 
def home(req):
    return HttpResponse("ders6")


# class studentgav(mixins.CreateModelMixin,mixins.ListModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=student_seria

#     def get(self,req,*args,**kwargs):
#         return self.list(req,*args,**kwargs)


#     def post(self,req,*args,**kwargs):
#         return self.create(req,*args,**kwargs)


# class studentdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=student_seria


#     def get(self,req,*args,**kwargs):
#         return self.retrieve(req,*args,**kwargs)


#     def put(self,req,*args,**kwargs):
#         return self.update(req,*args,**kwargs)

#     def delete(self,req,*args,**kwargs):
#         return self.destroy(req,*args,**kwargs)

class studentget(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class=student_seria

class studentdetail(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=student_seria
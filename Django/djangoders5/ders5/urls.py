
from django.urls import path
from .views import Student,home,student_list,create,details,putlama,silme
urlpatterns = [
    path("",Student),
    path("home/",home),
    path("studentlist/",student_list),
    path("create/",create),
    path("details/<int:pk>",details),
    path("putlama/<int:pk>",putlama),
    path("silme/<int:pk>",silme)
]

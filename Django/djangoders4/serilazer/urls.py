

from django.urls import path
from .views import serilazerlar,student_api_put,student_api


urlpatterns = [
   path("",serilazerlar) ,
   path("get/", student_api),
   path("put/<int:pk>", student_api_put)
]

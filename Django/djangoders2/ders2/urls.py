
from django.urls import path
from .views import ders2,der3
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("ders2",ders2),
    path("der3/",der3),
    
]

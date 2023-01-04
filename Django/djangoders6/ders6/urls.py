from django.urls import path
from .views import home
# from .views import studentdetail,studentgav
from .views import studentget,studentdetail


urlpatterns = [
    path('', home),
    # path("get",studentgav.as_view()),
    # path("details/<int:pk>",studentdetail.as_view())
    path("get",studentget.as_view()),
    path("details/<int:pk>",studentdetail.as_view())


]
 
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nuevo_alumno/', views.nuevo_alumno, name="nuevo_alumno"),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nuevo_examen/', views.nuevo_examen, name='index'),
]

from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.Login, name='Login'),
    url(r'^index/', views.Index, name='Index'),
    url(r'^logout/', views.Logout, name='Logout'),
    url(r'^nuevo_alumno/', views.NewStudent, name='NewStudent'),
    url(r'^nuevo_instructor/', views.NewInstructor, name='NewInstructor'),
    url(r'^nuevo_examen/', views.NewExam, name='NewExam'),
    url(r'^examen/(?P<exam_code>\w+)/$', views.ListExam, name='ListExam'),
]

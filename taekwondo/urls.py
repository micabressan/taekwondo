from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('examenes.urls')),
    url('', include('usuarios.urls')),
    url('', include('alumnos.urls')),
]

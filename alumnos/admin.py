# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from alumnos.models import (
            Alumno
    )


class AdminAlumnos(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'edad', 'ciudad', 'numero_libreta', 'categoria')
    list_filter = ('nombre', 'categoria', 'ciudad')
    search_fields = ('nombre', 'categoria', 'ciudad')

admin.site.register(Alumno, AdminAlumnos)

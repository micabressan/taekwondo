# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from alumnos.forms import NuevoAlumnoForm
from django.shortcuts import render

def nuevo_alumno(request):
    form = NuevoAlumnoForm
    return render(request, 'nuevo_alumno.html', {'form': form})

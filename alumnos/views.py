# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from alumnos.forms import NuevoAlumnoForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render

def nuevo_alumno(request):
    formulario_carga = NuevoAlumnoForm(request.POST)
    if request.method == 'POST':
        if formulario_carga.is_valid():
            alumno = formulario_carga.save(commit=False)
            alumno.save()
            return HttpResponseRedirect("/nuevo_alumno/")
    else:
        formulario_carga = NuevoAlumnoForm()

    ctx = {'form': formulario_carga}
    return render(request, "nuevo_alumno.html", ctx)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def nuevo_alumno(request):
    return render(request, 'nuevo_alumno.html', {})

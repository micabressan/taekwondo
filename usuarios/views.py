# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def index(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'login.html', {})

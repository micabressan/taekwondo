# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from usuarios.formularios import (
    login_form,
    )

def login(request):
    """vista login"""
    error_message = ""
    formulario_login = login_form(request.POST)
    if request.POST:
        if formulario_login.is_valid():
            username = formulario_login.cleaned_data['username']
            password = formulario_login.cleaned_data['password']
            current_user = authenticate(username=username,
                                        password=password)
            if current_user is not None and current_user.is_active:
                login_form(request, current_user)
                return HttpResponseRedirect('index/')
            else:
                error_message = "Usuario y/o contraseña incorrectos"
    formulario_login = login_form()
    return render(request, 'login.html', {'formulario_login': formulario_login,
                                        'error_message': error_message})


def index(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'login.html', {})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from usuarios.forms import (
    LoginForm,
    )

def login(request):
    """vista login template"""
    error_message = ""
    formulario_login = LoginForm(request.POST)
    if request.POST:
        if formulario_login.is_valid():
            username = formulario_login.cleaned_data['username']
            password = formulario_login.cleaned_data['password']
            current_user = authenticate(username=username,
                                        password=password)
            if current_user is not None and current_user.is_active:
                LoginForm(request, current_user)
                return HttpResponseRedirect('index/')
            else:
                error_message = "Usuario y/o contraseña incorrectos"
    formulario_login = LoginForm()
    return render(request, 'login.html', {'formulario_login': formulario_login,
                                        'error_message': error_message})


def index(request):
    """vista index template"""
    return render(request, 'index.html', {})

def logout(request):
    """vista logout template"""
    logout(request)
    return HttpResponseRedirect('login/')

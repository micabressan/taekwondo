# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate #, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from sitio.forms import (
    LoginForm,
    NewStudentForm,
    NewInstructorForm,
    NewExamForm,
    NewAlumnForExamForm,
    NewInstructorForExamForm,
    NewExaminingTableForm
    )

from sitio.models import (
    Examen,
    AlumnoPorExamen,
    InstructorPorExamen,
    MesaExaminadora
    )

def Index(request):
    """vista index template"""
    return render(request, 'index.html', {})


def Login(request):
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
    
    ctx = {'formulario_login': formulario_login,
            'error_message': error_message}
    
    return render(request, 'login.html', ctx)


def Logout(request):
    """vista logout template"""
    Logout(request)
    return HttpResponseRedirect('login/')


def NewStudent(request):
    """Vista de nuevo estudiante"""
    formulario_carga = NewStudentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if formulario_carga.is_valid():
            alumno = formulario_carga.save(commit=False)
            alumno.save()
            return HttpResponseRedirect("/nuevo_alumno/")
    else:
        formulario_carga = NewStudentForm()

    ctx = {'form': formulario_carga}
    return render(request, "nuevo_alumno.html", ctx)
    
    
def NewInstructor(request):
    """Vista de nuevo instructor"""
    formulario_carga = NewInstructorForm(request.POST)
    if request.method == 'POST':
        if formulario_carga.is_valid():
            instructor = formulario_carga.save(commit=False)
            instructor.save()
            return HttpResponseRedirect("/nuevo_instructor/")
    else:
        formulario_carga = NewInstructorForm()

    ctx = {'form': formulario_carga}
    return render(request, "nuevo_instructor.html", ctx)


def NewExam(request):
    """vista nuevo examen template"""
    formulario_carga = NewExamForm(request.POST)
    formulario_alumno = NewAlumnForExamForm(request.POST)
    formulario_instructor = NewInstructorForExamForm(request.POST)
    formulario_mesa = NewExaminingTableForm(request.POST)
    if request.method == 'POST':
        if formulario_carga.is_valid():
            examen = formulario_carga.save(commit=False)
            examen.save()
        
        if formulario_alumno.is_valid():
            alumno = formulario_carga.save(commit=False)
            alumno.save()
        
        if formulario_instructor.is_valid():
            instructor = formulario_instructor.save(commit=False)
            instructor.save()
        
        if formulario_mesa.is_valid():
            mesa = formulario_mesa.save(commit=False)
            mesa.save()
        return HttpResponseRedirect("/nuevo_examen/")
    else:
        formulario_carga = NewExamForm()
    
    all_instructor = InstructorPorExamen.objects.all()
    
    ctx = {'form': formulario_carga, 'alum': formulario_alumno, 
            'inst': formulario_instructor, 'mesa': formulario_mesa, 'datos': all_instructor}
    return render(request, 'nuevo_examen.html', ctx)


def ListExam(request, exam_code):
    Exam = Examen.objects.get(Codigo=exam_code)
    Alum = AlumnoPorExamen.objects.all()
    Inst = InstructorPorExamen.objects.all()
    Mesa = MesaExaminadora.objects.all()
    alumnos = []
    for alumno in Alum:
        if alumno.FechaExamen == Exam.Fecha:
            alumnos.append(alumno)
    
    ctx = {'examen' : Exam, 'alumno': alumnos, 
            'instructor': Inst, 'mesa': Mesa}
    
    return render(request, 'examen.html', ctx)
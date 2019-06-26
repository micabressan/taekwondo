# -*- coding: utf-8 -*-
from django import forms
from django.forms import Textarea, TextInput, Select, CheckboxInput, DateInput, ImageField
from sitio.models import (
    Alumno,
    Instructor,
    Examen,
    AlumnoPorExamen,
    InstructorPorExamen,
    MesaExaminadora
    )


class LoginForm(forms.Form):
    """Formulario login, utilizado en la vista y template de login"""
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                'class': 'form-control',
                                                'placeholder': 'Nombre de usuario'
                                                }))
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False, attrs={
                                                'class': 'form-control',
                                                'placeholder': "Contraseña"
                                                })
    )

class NewStudentForm(forms.ModelForm):
    """Formulario estudiante, utilizado en la vista y template de carga y 
    edicion de alumnos"""
    
    class Meta:
        model = Alumno
        fields = ('Nombre', 'Apellido', 'FechaNacimiento', 'Ciudad', 
                'Direccion', 'Celular', 'mail', 'FechaInicio', 'FechaFin',
                'NumeroLibreta', 'Categoria', 'Instructor', 'Observacion')
        widgets = {'Nombre': 
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Nombre',
                            }),
                    'Apellido':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Apellido',
                            }),
                    'FechaNacimiento':
                        DateInput(attrs={
                            'class':'form-control',
                            'placeholder':'Fecha de Nacimiento',
                            'type':'date',
                            }),
                    'Ciudad':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Direccion':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Direccion',
                            }),
                    'Celular':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Celular',
                            }),
                    'mail':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Email',
                            }),
                    'FechaInicio':
                        DateInput(attrs={
                            'class':'form-control',
                            'placeholder':'Fecha de Inicio',
                            'type':'date',
                            }),
                    'FechaFin':
                        DateInput(attrs={
                            'class':'form-control',
                            'placeholder':'Fecha de Fin',
                            'type':'date',
                            }),
                    'NumeroLibreta':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Número Libreta',
                            }),
                    'Categoria':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Instructor':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Observaciones':
                        Textarea(attrs={
                            'class':'form-control',
                            'placeholder':'Observaciones',
                            })}


class NewInstructorForm(forms.ModelForm):
    """Formulario de instructores, utilizado en la carga y edicion de instructores"""
    
    class Meta:
        model = Instructor
        fields = ('Nombre', 'Apellido', 'Ciudad', 'Categoria', 'FechaInicio',
                'FechaFin', 'CodigoAR', 'FechaCodigoAR', 'CodigoID', 'Licencia', 
                'EscuelaAnterior')
        widgets = {'Nombre': 
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Nombre',
                            }),
                    'Apellido':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Apellido',
                            }),
                    'Ciudad':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Categoria':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'FechaInicio':
                        DateInput(attrs={
                            'class':'form-control',
                            'type':'date',
                            }),
                    'FechaFin':
                        DateInput(attrs={
                            'class':'form-control',
                            'placeholder':'Fecha de Fin',
                            'type':'date',
                            }),
                    'CodigoAR':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Código AR',
                            }),
                    'FechaCodigoAR':
                        DateInput(attrs={
                            'class':'form-control',
                            'type': 'date',
                            }),
                    'CodigoID':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder': 'Código ID',
                            }),
                    'Licencia':
                        TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Número licencia',
                            }),
                    'EscuelaAnterior':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Escuela Anterior',
                            })}
 

class NewExamForm(forms.ModelForm):
    """Formulario de examen utilizado en la carga y edicion de examenes"""

    class Meta:
        model = Examen
        fields = ('Fecha', 'Ciudad', 'InstructorMayor')
        widgets = {'Fecha':
                        DateInput(attrs={
                            'class':'form-control',
                            'type':'date',
                            }),
                    'Ciudad':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'InstructorMayor':
                        Select(attrs={
                            'class':'form-control',
                            })}


class NewAlumnForExamForm(forms.ModelForm):
    
    class Meta:
        model = AlumnoPorExamen
        fields = ('FechaExamen', 'Alumno', 'Categoria', 'Examinador', 'Observaciones')
        widgets = {'FechaExamen':
                        DateInput(attrs={
                            'class':'form-control',
                            'type':'date',
                            }),
                    'Alumno':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Categoria':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Examinador':
                        Select(attrs={
                            'class':'form-control',
                            }),
                    'Observaciones':
                        Textarea(attrs={
                            'class':'form-control',
                            })}


class NewInstructorForExamForm(forms.ModelForm):

    class Meta:
        model = InstructorPorExamen
        fields = ('Instructor',)
        widgets = {'Instructor':
                        Select(attrs={
                            'class':'form-control',
                            })}


class NewExaminingTableForm(forms.ModelForm):

    class Meta:
        model = MesaExaminadora
        fields = ('Instructor',)
        widgets = {'Instructor':
                        Select(attrs={
                            'class':'form-control',
                            })}
# -*- coding: utf-8 -*-
from django import forms
from django.forms import Textarea, TextInput, Select, CheckboxInput


class login_form(forms.Form):
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

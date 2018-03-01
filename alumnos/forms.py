from django import forms
from django.forms import TextInput, Select, Textarea, DateInput
from alumnos.models import Alumno

class NuevoAlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'fecha_nacimiento', 'ciudad', 'numero_libreta', 'categoria', 'observaciones',)
        widgets = {'nombre': 
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Nombre',
                            }),
                  'apellido':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Apellido',
                            }),
                  'fecha_nacimiento':
                        DateInput(attrs={
                            'class':'form-control',
                            'placeholder':'Fecha de Nacimiento',
                            'type':'date',
                            }),
                  'ciudad':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Ciudad',
                            }),
                  'numero_libreta':
                        TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Número Libreta',
                            }),
                  'categoria':
                        Select(attrs={
                            'class':'form-control',
                            }),
                  'observaciones':
                        Textarea(attrs={
                            'class':'form-control',
                            'placeholder':'Observaciones',
                            })}
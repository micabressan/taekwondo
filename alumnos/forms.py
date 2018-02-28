from django import forms
from django.forms import TextInput, Select
from alumnos.models import Alumno

class NuevoAlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'edad', 'ciudad', 'numero_libreta', 'categoria',)
        widgets = {'nombre': TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
                  'apellido': TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}),
                  'edad': TextInput(attrs={'class':'form-control', 'placeholder':'Edad'}),
                  'ciudad': TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
                  'numero_libreta': TextInput(attrs={'class':'form-control', 'placeholder':'Numero Libreta'}),
                  'categoria': Select(attrs={'class':'form-control'}),}
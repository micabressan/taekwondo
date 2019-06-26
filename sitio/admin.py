from django.contrib import admin

from sitio.models import (
    Alumno, 
    Categoria, 
    Ciudad, 
    Instructor, 
    Examen, 
    AlumnoPorExamen, 
    InstructorPorExamen, 
    MesaExaminadora, 
    Curso,
    AlumnoPorCurso, 
    Torneo, 
    AlumnoPorTorneo
    )
    
    
class AdminCategorias(admin.ModelAdmin):
    list_display = ('Codigo', 
                    'Categoria', 
                    'Color')
    

class AdminCiudades(admin.ModelAdmin):
    list_display = ('Codigo', 
                    'Descripcion')
    
    
class AdminInstructores(admin.ModelAdmin):
    list_display = ('Codigo', 
                    'Nombre', 
                    'Apellido', 
                    'Ciudad', 
                    'Categoria', 
                    'FechaInicio', 
                    'FechaFin', 
                    'CodigoAR', 
                    'FechaCodigoAR', 
                    'CodigoID', 
                    'Licencia', 
                    'EscuelaAnterior')
    list_filter = ('Nombre', 
                    'Apellido', 
                    'Ciudad', 
                    'Categoria', 
                    'FechaInicio', 
                    'FechaFin', 
                    'CodigoAR', 
                    'FechaCodigoAR', 
                    'CodigoID', 
                    'Licencia', 
                    'EscuelaAnterior')
    search_fields = ('Nombre', 
                    'Apellido', 
                    'Ciudad', 
                    'Categoria', 
                    'FechaInicio', 
                    'FechaFin', 
                    'CodigoAR', 
                    'FechaCodigoAR', 
                    'CodigoID', 
                    'Licencia', 
                    'EscuelaAnterior')    
    

class AdminAlumnos(admin.ModelAdmin):
    list_display = ('Codigo', 
                    'Nombre', 
                    'Apellido', 
                    'FechaNacimiento', 
                    'Ciudad', 
                    'NumeroLibreta', 
                    'Categoria')
    list_filter = ('Nombre', 
                    'Categoria', 
                    'Ciudad')
    search_fields = ('Nombre', 
                    'Categoria', 
                    'Ciudad')


class AdminExamenes(admin.ModelAdmin):
    list_display = ('Codigo',
                    'Fecha',
                    'Ciudad',
                    'InstructorMayor')
    list_filter = ('Ciudad',
                    'InstructorMayor')
    search_fields = ('Ciudad',
                    'InstructorMayor')
    

class AdminAlumnosPorExamenes(admin.ModelAdmin):
    list_display = ('Codigo',
                    'FechaExamen',
                    'Alumno',
                    'Categoria',
                    'Examinador',
                    'Observaciones')
    list_filter = ('FechaExamen',
                    'Alumno',
                    'Examinador')
    search_fields = ('FechaExamen',
                    'Alumno',
                    'Examinador')


class AdminInstructoresPorExamenes(admin.ModelAdmin):
    list_display = ('Codigo',
                    'FechaExamen',
                    'Instructor')
    list_filter = ('FechaExamen',
                    'Instructor')
    search_fields = ('FechaExamen',
                    'Instructor')


class AdminMesaExaminadora(admin.ModelAdmin):
    list_display = ('Codigo',
                    'FechaExamen',
                    'Instructor')
    list_filter = ('FechaExamen',
                    'Instructor')
    search_fields = ('FechaExamen',
                    'Instructor')


class AdminCursos(admin.ModelAdmin):
    list_display = ('Codigo',
                    'Nombre',
                    'Ciudad',
                    'Fecha',
                    'Descripcion')
    list_filter = ('Nombre',
                    'Ciudad',
                    'Fecha')
    search_fields = ('Nombre',
                    'Ciudad',
                    'Fecha')


class AdminAlumnosPorCursos(admin.ModelAdmin):
    list_display = ('Codigo',
                    'Curso',
                    'Alumno')
    list_filter = ('Curso',
                    'Alumno')
    search_fields = ('Curso',
                    'Alumno')


class AdminTorneos(admin.ModelAdmin):
    list_display = ('Codigo',
                    'Fecha',
                    'Ciudad',
                    'Direccion',
                    'Organizador',
                    'Observacion')
    list_filter = ('Ciudad',
                    'Organizador')
    search_fields = ('Ciudad',
                    'Organizador')


class AdminAlumnosPorTorneos(admin.ModelAdmin):
    list_display = ('Codigo',
                    'Torneo',
                    'Alumno')
    list_filter = ('Torneo',
                    'Alumno')
    search_fields = ('Torneo',
                    'Alumno')
    
    
admin.site.register(Categoria, AdminCategorias)
admin.site.register(Ciudad, AdminCiudades)
admin.site.register(Instructor, AdminInstructores)
admin.site.register(Alumno, AdminAlumnos)
admin.site.register(Examen, AdminExamenes)
admin.site.register(AlumnoPorExamen, AdminAlumnosPorExamenes)
admin.site.register(InstructorPorExamen, AdminInstructoresPorExamenes)
admin.site.register(MesaExaminadora, AdminMesaExaminadora)
admin.site.register(Curso, AdminCursos)
admin.site.register(AlumnoPorCurso, AdminAlumnosPorCursos)
admin.site.register(Torneo, AdminTorneos)
admin.site.register(AlumnoPorTorneo, AdminAlumnosPorTorneos)
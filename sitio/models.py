from __future__ import unicode_literals

from django.db import models


class Ciudad(models.Model):
    """Modelo de ciudades"""
    Codigo = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.Descripcion
    
    class Meta:
        verbose_name_plural = "Ciudades"
  
    
class Categoria(models.Model):
    """Modelo de categorias"""
    Codigo = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=20)
    Color = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.Categoria
    
    class Meta:
        verbose_name_plural = "Categorias"


class Instructor(models.Model): 
    """Modelo de instructores"""
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=25)
    Ciudad = models.ForeignKey(Ciudad, null=False)
    Categoria = models.ForeignKey(Categoria, null=False)
    FechaInicio = models.DateField()
    FechaFin = models.DateField(blank=True, null=True)
    CodigoAR = models.CharField(max_length=9) #ID de los cinturones negros
    FechaCodigoAR = models.DateField()
    CodigoID = models.IntegerField(max_length=6)
    Licencia = models.IntegerField(max_length=6, blank=True, null=True) #Placa de instructores
    EscuelaAnterior = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
        return self.Nombre + ' ' + self.Apellido

    class Meta:
        verbose_name_plural = "Instructores"


class Alumno(models.Model):
    """Modelo de alumnos"""
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    FechaNacimiento = models.DateField(null=False)
    Ciudad = models.ForeignKey(Ciudad)
    Direccion = models.CharField(max_length=100, blank=True, null=True)
    Celular = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    FechaInicio = models.DateField(null=False)
    FechaFin = models.DateField(blank=True, null=True)
    NumeroLibreta = models.IntegerField(unique=True)
    Categoria = models.ForeignKey(Categoria, null=False)
    Instructor = models.ForeignKey(Instructor, null=False)
    Observacion = models.CharField(max_length=200, default='', blank=True, null=True)
    Imagen = models.ImageField(upload_to= 'static/fotos', blank=True, null=True)

    def __str__(self):
        return self.Nombre + ' ' + self.Apellido
    
    class Meta:
        verbose_name_plural = "Alumnos"
    

class Examen(models.Model):
    """Modelo de un nuevo examen"""
    Codigo = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Ciudad = models.ForeignKey(Ciudad, null=False)
    InstructorMayor = models.ForeignKey(Instructor, null=False)

    def __str__(self):
        return str(self.Fecha)

    class Meta:
        verbose_name_plural = "Examen"
    
    
class AlumnoPorExamen(models.Model):
    """Modelo de examen por alumno"""
    Codigo = models.AutoField(primary_key=True)
    FechaExamen = models.ForeignKey(Examen, null=False)
    Alumno = models.ForeignKey(Alumno, null=False)
    Categoria = models.ForeignKey(Categoria, null=False)
    Examinador = models.ForeignKey(Instructor, null=False)
    Observaciones = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Alumnos por examen"


class InstructorPorExamen(models.Model):
    """Modelo de insturctores por examen"""
    Codigo = models.AutoField(primary_key=True)
    FechaExamen = models.ForeignKey(Examen, null=False)
    Instructor = models.ForeignKey(Instructor, null=False)
    
    class Meta:
        verbose_name_plural = "Instructores por examen"


class MesaExaminadora(models.Model):
    """Modelo de mesa examinadora"""
    Codigo = models.AutoField(primary_key=True)
    FechaExamen = models.ForeignKey(Examen, null=False)
    Instructor = models.ForeignKey(Instructor, null=False)
    
    class Meta:
        verbose_name_plural = "Mesas examinadoras"
    

class Curso(models.Model):
    """Modelo de cursos y/o capacitaciones"""
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Ciudad = models.ForeignKey(Ciudad, null=False)
    Fecha = models.DateField()
    Descripcion = models.CharField(max_length=500, blank=True, null=True)
    Imagen = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.Nombre
    
    class Meta:
        verbose_name_plural = "Cursos"


class AlumnoPorCurso(models.Model):
    """Modelo de estudiante por curso y/o capacitaciones"""
    Codigo = models.AutoField(primary_key=True)
    Curso = models.ForeignKey(Curso, null=False)
    Alumno = models.ForeignKey(Alumno, null=False)
    
    class Meta:
        verbose_name_plural = "Alumnos por cursos"
    

class Torneo(models.Model):
    """Modelo de torneos"""
    Codigo = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Ciudad = models.ForeignKey(Ciudad, null=False)
    Direccion = models.CharField(max_length=100)
    Organizador = models.CharField(max_length=200)
    Observacion = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return str(self.Fecha)
    
    class Meta:
        verbose_name_plural = "Torneos"
    

class AlumnoPorTorneo(models.Model):
    """Modelo de estudiantes por competicion"""
    Codigo = models.AutoField(primary_key=True)
    Torneo = models.ForeignKey(Torneo, null=False)
    Alumno = models.ForeignKey(Alumno, null=False)
    
    class Meta:
        verbose_name_plural = "Alumnos por Torneos"
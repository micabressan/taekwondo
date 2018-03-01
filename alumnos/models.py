# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.fields import AutoField, CharField, IntegerField, SmallIntegerField, DateField
from django.db import models

class Alumno(models.Model):
    CATEGORIAS = (
        (10, 'Blanco (10º GUP)'),
        (9, 'Punta Amarilla (9º GUP)'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=20)
    numero_libreta = models.IntegerField(unique=True)
    categoria = models.SmallIntegerField(choices=CATEGORIAS)
    observaciones = models.CharField(max_length=200, default='')

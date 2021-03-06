# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-04 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=20)),
                ('FechaNacimiento', models.DateField()),
                ('Direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('Celular', models.CharField(blank=True, max_length=15, null=True)),
                ('mail', models.CharField(blank=True, max_length=50, null=True)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField(blank=True, null=True)),
                ('NumeroLibreta', models.IntegerField(unique=True)),
                ('Observacion', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='static/fotos')),
            ],
            options={
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='AlumnoPorCurso',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Alumno')),
            ],
            options={
                'verbose_name_plural': 'Alumnos por cursos',
            },
        ),
        migrations.CreateModel(
            name='AlumnoPorExamen',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Alumno')),
            ],
            options={
                'verbose_name_plural': 'Alumnos por examen',
            },
        ),
        migrations.CreateModel(
            name='AlumnoPorTorneo',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Alumno')),
            ],
            options={
                'verbose_name_plural': 'Alumnos por Torneos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Categoria', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200)),
                ('Fecha', models.DateField()),
                ('Descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Examen',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=25)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField(blank=True, null=True)),
                ('CodigoAR', models.CharField(max_length=9)),
                ('FechaCodigoAR', models.DateField()),
                ('CodigoID', models.IntegerField(max_length=6)),
                ('Licencia', models.IntegerField(blank=True, max_length=6, null=True)),
                ('EscuelaAnterior', models.CharField(blank=True, max_length=25, null=True)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Categoria')),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Instructores',
            },
        ),
        migrations.CreateModel(
            name='InstructorPorExamen',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('FechaExamen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Examen')),
                ('Instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Instructor')),
            ],
            options={
                'verbose_name_plural': 'Instructores por examen',
            },
        ),
        migrations.CreateModel(
            name='MesaExaminadora',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('FechaExamen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Examen')),
                ('Instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Instructor')),
            ],
            options={
                'verbose_name_plural': 'Mesas examinadoras',
            },
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Direccion', models.CharField(max_length=100)),
                ('Organizador', models.CharField(max_length=200)),
                ('Observacion', models.CharField(blank=True, max_length=500, null=True)),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Torneos',
            },
        ),
        migrations.AddField(
            model_name='examen',
            name='InstructorMayor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Instructor'),
        ),
        migrations.AddField(
            model_name='alumnoportorneo',
            name='Torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Torneo'),
        ),
        migrations.AddField(
            model_name='alumnoporexamen',
            name='Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Categoria'),
        ),
        migrations.AddField(
            model_name='alumnoporexamen',
            name='Examinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Instructor'),
        ),
        migrations.AddField(
            model_name='alumnoporexamen',
            name='FechaExamen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Examen'),
        ),
        migrations.AddField(
            model_name='alumnoporcurso',
            name='Curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Categoria'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Ciudad'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='Instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Instructor'),
        ),
    ]

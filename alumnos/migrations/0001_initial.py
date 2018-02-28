# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('ciudad', models.CharField(max_length=10)),
                ('numero_libreta', models.IntegerField()),
                ('categoria', models.SmallIntegerField(choices=[(10, 'Blanco (10\xba GUP)'), (9, 'Punta Amarilla (9\xba GUP)')])),
            ],
        ),
    ]

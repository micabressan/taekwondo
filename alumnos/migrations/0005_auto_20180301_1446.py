# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-01 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_auto_20180301_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='numero_libreta',
            field=models.IntegerField(unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetario', '0004_remove_receta_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]

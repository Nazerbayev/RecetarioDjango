from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


@python_2_unicode_compatible
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True)
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return self.titulo


@python_2_unicode_compatible
class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre




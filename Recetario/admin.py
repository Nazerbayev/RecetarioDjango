from django.contrib import admin

from Recetario.models import Question, Receta, Ingrediente

admin.site.register(Question)
admin.site.register(Receta)
admin.site.register(Ingrediente)

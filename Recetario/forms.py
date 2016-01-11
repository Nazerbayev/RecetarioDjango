#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from Recetario.models import Receta


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["titulo", "preparacion", "descripcion", "imagen"]
        error_messages = {
            "required": "%(model_name) - %(field_labels) es requerido"
        }


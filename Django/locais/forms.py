# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from locais.models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=["locais", "nome", "comentario", "avaliacao"]




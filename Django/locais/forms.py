# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from locais.models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=["locais", "nome", "comentario", "avaliacao"]



class CommentForm(forms.Form):
    locais = forms.CharField(label='Login', max_length=50)
    nome = forms.CharField(label='Senha', max_length=50)
    comentario = forms.CharField(label='Senha', max_length=50)
    avaliacao = forms.CharField(label='Senha', max_length=50)
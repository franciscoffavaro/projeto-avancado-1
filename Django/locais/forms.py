# -*- coding: utf-8 -*-

from django import forms
from django.forms import *
from locais.models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=["locais", "nome", "comentario", "avaliacao"]


        CHOICES= (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            )
        widgets = {
            'avaliacao': Select(choices=CHOICES),
        }


#class UserForm(forms.Form):
#    login = forms.CharField(label='Login', max_length=50)
#    senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput())
#    telefone = forms.CharField(label='Telefone', max_length=20)
#    endereco = forms.CharField(label='Endereço', max_length=150)

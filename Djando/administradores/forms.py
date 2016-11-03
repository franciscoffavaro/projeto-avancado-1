# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from locais.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields=["autor", "titulo_local", "descricao", "categorias", "latitude", "longitude", "imagem"]

class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=50)
    senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput())

class UserForm(forms.Form):
    login = forms.CharField(label='Login', max_length=50)
    senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput())
    telefone = forms.CharField(label='Telefone', max_length=20)
    endereco = forms.CharField(label='Endereço', max_length=150)

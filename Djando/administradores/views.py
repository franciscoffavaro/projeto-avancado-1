# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth.decorators import login_required
from .models import *
from administradores.forms import *

#Função que autentica o usuário na tela de Login do Sistema
def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form_login = form.cleaned_data['login']
            form_senha = form.cleaned_data['senha']

            user = authenticate(username=form_login, password=form_senha)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/local/index/')
    else:
        form = LoginForm()

    return render(request, 'administradores/login.html', {'form':form})


def user_new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            login = form.cleaned_data['login']
            senha = form.cleaned_data['senha']
            telefone = form.cleaned_data['telefone']
            endereco = form.cleaned_data['endereco']
            new_user = User.objects.create_user(login, password=senha)
            new_user.save()
            new_profile = UserAdmin(user=new_user, telefone=telefone, endereco=endereco)
            new_profile.save()
            return HttpResponseRedirect('/local/index/')

    else:
        form = UserForm()
    return render(request, 'administradores/newuser.html', {'form':form})

#Adição de um novo Local
@login_required
def local_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('/local/index/')
    else:
        form = PostForm();
    return render(request, 'administradores/novo_local_restrict.html', {'form':form})

#Ecição de um local usando como parâmetro seu ID
@login_required
def local_edit(request, locais_post_id):
    local = Post.objects.get(pk=locais_post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=local)
        form.save()
        return HttpResponseRedirect('/local/index/')
    else:
        form = PostForm(instance=local)

    return render(request, 'administradores/editar_local.html', {'form':form, 'local_id': locais_post_id})

#Remoção de um Local do Sistema usando como parâmetro seu ID.
@login_required
def local_delete(request, locais_post_id):
    local = Post.objects.get(pk=locais_post_id)
    local.delete()
    return HttpResponseRedirect('/local/index/')

@login_required
def local_index(request):
    locais = Post.objects.all()
    users = UserAdmin.objects.all()

    return render (request, 'administradores/restrict_area.html', {'locais':locais, 'users':users})

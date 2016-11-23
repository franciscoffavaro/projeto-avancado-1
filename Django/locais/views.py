from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from .models import *
from .forms import *

def post_index(request):
    locais=Local.objects.all()
    return render(request, 'locais/index.html', {'locais':locais})

def post_avaliacoes(request):
    return render(request, 'locais/avaliacoes.html', {})

def post_telefonesUteis(request):
    return render(request, 'locais/listaTelefonesUteis.html', {})

def post_contato(request):
    return render(request, 'locais/contato.html', {})

def post_categorias(request):
    return render (request, 'locais/lista_locais.html', {})

def locais_detalhes(request, locais_post_id):
    local = Local.objects.get(pk=locais_post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
    else:
        form = CommentForm();
    return render (request, 'locais/locais_descricao.html', {'local':local, 'form':form})

def comment_locais(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
    else:
        form = CommentForm();
    return render(request, 'locais/locais_descricao.html', {'form':form})




# Create your views here.

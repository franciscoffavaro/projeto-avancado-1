from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from .models import Post

def post_index(request):
    locais=Post.objects.all()
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
    local = Post.objects.get(pk=locais_post_id)
    return render (request, 'locais/locais_descricao.html', {'local':local})



# Create your views here.

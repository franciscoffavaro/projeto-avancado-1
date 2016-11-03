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

<<<<<<< HEAD
def post_categorias(request):
    locais=Post.objects.all()
    return render (request, 'locais/lista_locais.html', {'locais':locais})
=======
def post_academia(request):
    return render(request, 'locais/academia.html',{})

def post_academiadescricao(request):
    return render(request,'locais/academiadescricao.html',{})
>>>>>>> 4f058dde863ff308ca2dda8ee638d406922cd77f

# Create your views here.

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Post

def post_index(request):
    locais=Post.objects.all()
    return render(request, 'locais/index.html', {'locais':locais})

def post_avaliacoes(request):
    return render(request, 'locais/avaliacoes.html', {})

def post_telefonesUteis(request):
    return render(request, 'locais/listaTelefonesUteis.html', {})

def post_login(request):
    return render(request, 'locais/telaLogin.html', {})

def post_contato(request):
    return render(request, 'locais/contato.html', {})

def post_academia(request):
    return render(request, 'locais/academia.html',{})

def post_academiadescricao(request):
    return render(request,'locais/academiadescricao.html',{})

# Create your views here.

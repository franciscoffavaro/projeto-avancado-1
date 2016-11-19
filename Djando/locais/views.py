from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from .models import *
from .forms import *
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

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

def locais_detalhes(request):
    local1 = Local.objects.all()
    local = serializers.serialize("json", Local.objects.all())


    print(local)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
    else:
        form = CommentForm();
    return render (request, 'locais/academiamobile.html', {'local':local, 'form':form})


def locais_json(request):

        local1 = Local.objects.all()
        local = serializers.serialize("json", Local.objects.all())
        queryset = Local.objects.values('pk', 'autor' ,'titulo_local','descricao', 'categorias', 'latitude','longitude','imagem')

        print(list(queryset))
        if request.method == 'POST':
            form = CommentForm(request.POST)
            form.save()
        else:
            form = CommentForm();


        return JsonResponse(list(queryset), safe=False)


def post_listaTelefonicaMobile(request):
    return render (request, 'locais/listaTelefonicaMobile.html', {})
def post_contatomobile(request):
    return render (request, 'locais/contatomobile.html', {})




# Create your views here.

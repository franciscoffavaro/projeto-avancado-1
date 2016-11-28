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
from geoposition.fields import GeopositionField
from django.template import RequestContext
from django.core.mail import send_mail


def post_index(request):
    locais=Local.objects.all()
    return render(request, 'locais/index.html', {'locais':locais})

def post_avaliacoes(request):
    return render(request, 'locais/avaliacoes.html', {})

def post_telefonesUteis(request):
    return render(request, 'locais/listaTelefonesUteis.html', {})

def post_contato(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid:
            nome = request.POST.get('nome', '')
            email = request.POST.get('email','')
            mensagem = request.POST.get('mensagem','')
            send_mail(email, mensagem, email, ['timeguiart@gmail.com'])
            HttpResponse("Email enviado")
            form = Contactform();
    else:
        form = Contactform();
    return render(request, 'locais/contato.html', {'form':form})

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

def locais_categoria(request, locais_categoria):
    locais = Local.objects.filter(categorias=locais_categoria)
    return render (request, 'locais/categorias.html', {'locais':locais})



def rec(n1,n2):
    locais=[]
    for i in range (n1,n2):

            try:
                temp=Local.objects.get(pk=i)
                local={}
                local["pk"]=temp.pk
                local["autor"]=temp.autor
                local["titulo_local"]=temp.titulo_local
                local["descricao"]=temp.descricao
                local["latitude"]=str(temp.position.latitude)
                local["longitude"]=str(temp.position.longitude)
                local["categorias"]=temp.categorias
                local["imagem"]=str(temp.imagem)

                locais.append(local)
            except (Exception):
                rec(i+1,n2)

    return (locais)


def locais_json(request):

        local1 = Local.objects.all()

        x=(Local.objects.latest('pk').pk)+1

        local = rec(1,x+1)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            form.save()
        else:
            form = CommentForm();

        return JsonResponse(list(local), safe=False)

def comentarios_json(request):

        queryset = Comment.objects.values('pk','locais', 'nome','comentario','avaliacao')

        if request.method == 'POST':
            form = CommentForm(request.POST)
            form.save()
        else:
            form = CommentForm();

        return JsonResponse(list(queryset), safe=False)

def post_academiasmobile(request):
    return render (request, 'locais/academiamobile.html', {})
def post_listaTelefonicaMobile(request):
    return render (request, 'locais/listaTelefonicaMobile.html', {})
def post_contatomobile(request):
    return render (request, 'locais/contatomobile.html', {})
def post_bancosmobile(request):
    return render (request, 'locais/bancosmobile.html', {})
def post_indexmobile(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
        return HttpResponseRedirect('/local/index_mobile/')
    else:
        return render (request, 'locais/indexmobile.html', {})
def post_restaurantemobile(request):
    return render (request, 'locais/restaurantemobile.html', {})
def post_localdescmobile(request, local_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
        return HttpResponseRedirect('/index_mobile/')
    else:
        form = CommentForm();
        return render (request, 'locais/locais_descricaoMobile.html', {"localid": local_id,'form':form})

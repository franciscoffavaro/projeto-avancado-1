# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from geoposition.fields import GeopositionField
from PIL import Image

class Local(models.Model):
    Academias='academia'
    Bancos='bancos'
    Saude_Medicina="saudemedicina"
    Hoteis_Pousadas='hoteispousadas'
    Organizacoes_Religiosas='religiosas'
    Beleza='beleza'
    Bares_Restaurantes_Lanchonetes='barrestlanch'
    Supermercados_Conveniencias='superconv'
    Casas_Shows_Eventos='casashoweventos'
    Educacao='educacao'
    Outros='outros'
    CHOICE_CATEGORIAS=((Academias, 'Academias'),(Bancos,'Bancos'),(Saude_Medicina, 'Saúde e Medicina'),(Hoteis_Pousadas, 'Hotéis e Pousadas'),
    (Organizacoes_Religiosas, 'Organizações Religiosas'), (Beleza, 'Beleza'), (Bares_Restaurantes_Lanchonetes,'Bar, Restaurantes e Lanchonetes'),
    (Supermercados_Conveniencias, 'Supermercados e Conveniências'),(Casas_Shows_Eventos, 'Casas de Shows e Eventos'),(Educacao, 'Educação'),(Outros, 'Outros'),
    )
    autor = models.CharField(max_length=200)
    titulo_local = models.CharField(max_length=200)
    descricao = models.TextField()
    categorias = models.CharField(max_length=40, choices=CHOICE_CATEGORIAS)
    position = GeopositionField(default=u'-6.8078347, -35.07674689999999', verbose_name=u'Geolocalização', help_text="Não altere os valores calculados automaticamente de latitude e longitude")
    imagem = models.ImageField(upload_to = "locais/images/", blank=True)

    def __str__(self):
        return self.titulo_local


class Comment(models.Model):
    locais = models.ForeignKey('Local', on_delete=models.CASCADE, default='')
    nome = models.CharField(max_length=50)
    comentario = models.TextField()
    avaliacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Contact (models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()

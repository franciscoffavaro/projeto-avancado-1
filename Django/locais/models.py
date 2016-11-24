# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from geoposition.fields import GeopositionField

class Local(models.Model):
    Academias='Academia'
    Bancos='Bancos'
    Saude_Medicina="SM"
    Hoteis_Pousadas='HP'
    Organizacoes_Religiosas='OR'
    Beleza='BL'
    Bares_Restaurantes_Lanchonetes='BRL'
    Supermercados_Conveniencias='SC'
    Casas_Shows_Eventos='CSE'
    Educacao='Educacao'
    Outros='Outros'
    CHOICE_CATEGORIAS=((Academias, 'Academias'),(Bancos,'Bancos'),(Saude_Medicina, 'SM'),(Hoteis_Pousadas, 'HP'),
    (Organizacoes_Religiosas, 'OR'), (Beleza, 'BL'), (Bares_Restaurantes_Lanchonetes,'BRL'),
    (Supermercados_Conveniencias, 'SC'),(Casas_Shows_Eventos, 'CSE'),(Educacao, 'Educacao'),(Outros, 'Outros'),
    )
    autor = models.CharField(max_length=200)
    titulo_local = models.CharField(max_length=200)
    descricao = models.TextField()
    categorias = models.CharField(max_length=40, choices=CHOICE_CATEGORIAS)
    position = GeopositionField(verbose_name=u'Geolocalização', help_text="Não altere os valores calculados automaticamente de latitude e longitude")
    imagem = models.ImageField(upload_to = "locais/static/images/postagem", blank=True)

    def __str__(self):
        return self.titulo_local


class Comment(models.Model):
    locais = models.ForeignKey('Local', on_delete=models.CASCADE, default='')
    nome = models.CharField(max_length=50)
    comentario = models.TextField()
    avaliacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

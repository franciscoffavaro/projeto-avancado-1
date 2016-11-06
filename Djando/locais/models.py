# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    Academias='Academia'
    Bancos='Bancos'
    Saude_Medicina="Saúde e Medicina"
    Hoteis_Pousadas='Hoteis e Pousadas'
    Organizacoes_Religiosas='Organizações Religiosas'
    Beleza='Beleza'
    Bares_Restaurantes_Lanchonetes='Bares, Restaurantes e Lanchonetes'
    Supermercados_Conveniencias='Supermercados e Conveniência'
    Casas_Shows_Eventos='Casas de Shows e Eventos'
    Educacao='Educação'
    Outros='Outros'
    CHOICE_CATEGORIAS=((Academias, 'Academias'),(Bancos,'Bancos'),(Saude_Medicina, 'Saude_Medicina'),(Hoteis_Pousadas, 'Hoteis_Pousadas'),
    (Organizacoes_Religiosas, 'Organizacoes_Religiosas'), (Beleza, 'Beleza'), (Bares_Restaurantes_Lanchonetes,'Bares_Restaurantes_Lanchonetes'),
    (Supermercados_Conveniencias, 'Supermercados_Conveniencias'),(Casas_Shows_Eventos, 'Casas_Shows_Eventos'),(Educacao, 'Educacao'),(Outros, 'Outros'),
    )
    autor = models.CharField(max_length=200)
    titulo_local = models.CharField(max_length=200)
    descricao = models.TextField()
    categorias = models.CharField(max_length=40, choices=CHOICE_CATEGORIAS)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    imagem = models.ImageField(upload_to = "locais/static/images/postagem", blank=True)

    def publich():
        self.save()

    def __str__(self):
        return self.titulo_local

class Avaliacao(models.Model):
    comentario = models.CharField(max_length=500)
    valor_avaliacao = models.IntegerField(default=0)

    def __str__(self):
        return self.comentario

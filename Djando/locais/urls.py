from django.conf.urls import include, url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.post_index, name='index'),
    #url(r'(?P<categoria>\w+)/$', views.post_categorias, name='categoria'),
    #url(r'(?P<categoria>\w+)/(?P<locai_id>\d+)/$', views.post_detalhes, name='detalhes'),
    url(r'^categorias/', views.post_categorias, name='categorias'),
    url(r'^avaliacoes/', views.post_avaliacoes, name='avaliacoes'),
    url(r'^telefones_uteis/', views.post_telefonesUteis, name='telefones_uteis'),
    url(r'^contato/', views.post_contato, name='contato'),
=======
    url(r'^$', views.post_index),
    url(r'^avaliacoes/', views.post_avaliacoes),
    url(r'^telefones/', views.post_telefonesUteis),
    url(r'^login/', views.post_login),
    url(r'^contato/', views.post_contato),
    url(r'^academia/', views.post_academia),
    url(r'^academiadescricao/', views.post_academiadescricao),

>>>>>>> 4f058dde863ff308ca2dda8ee638d406922cd77f
]

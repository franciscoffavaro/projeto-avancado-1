from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_index, name='index'),
    #url(r'(?P<locais_post_categorias>\w+)/$', views.post_categorias, name='categoria'),
    url(r'^local/(?P<locais_post_id>[0-9]+)/detalhes/', views.locais_detalhes, name='detalhes'),
    url(r'^telefones_uteis/', views.post_telefonesUteis, name='telefones_uteis'),
    url(r'^contato/', views.post_contato, name='contato'),
    url(r'^categoria/(?P<locais_categoria>[A-Z a-z]+)/$', views.locais_categoria, name='categorias'),

    url(r'^local/json', views.locais_json, name='json'),
    url(r'^index_mobile/', views.post_indexmobile, name='indexmobile'),
    url(r'^academias_mobile/', views.post_academiasmobile, name='academiamobile'),
    url(r'^telefones_uteis_mobile/', views.post_listaTelefonicaMobile, name='tel'),
    url(r'^contato_mobile/', views.post_contatomobile, name='contato_mobile'),
    url(r'^bancos_mobile/', views.post_bancosmobile, name='bancos_mobile'),
    url(r'^restaurante_mobile/', views.post_restaurantemobile, name='restaurante_mobile'),
    url(r'^localdesc_mobile/(?P<locais_categoria>[0-9]+)/$', views.post_localdescmobile, name='restaurante_mobile'),


]

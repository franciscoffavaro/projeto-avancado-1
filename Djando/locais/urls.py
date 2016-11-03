from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_index, name='index'),
    #url(r'(?P<categoria>\w+)/$', views.post_categorias, name='categoria'),
    #url(r'(?P<categoria>\w+)/(?P<locai_id>\d+)/$', views.post_detalhes, name='detalhes'),
    url(r'^categorias/', views.post_categorias, name='categorias'),
    url(r'^avaliacoes/', views.post_avaliacoes, name='avaliacoes'),
    url(r'^telefones_uteis/', views.post_telefonesUteis, name='telefones_uteis'),
    url(r'^contato/', views.post_contato, name='contato'),
]

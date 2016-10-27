from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_index),
    url(r'^avaliacoes/', views.post_avaliacoes),
    url(r'^telefones/', views.post_telefonesUteis),
    url(r'^login/', views.post_login),
    url(r'^contato/', views.post_contato),
]

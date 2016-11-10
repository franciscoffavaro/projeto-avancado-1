from django.conf.urls import url, include
from django.contrib import admin
from locais.models import *
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^local/index/$', views.local_index, name='index_restrict'),
    url(r'^local/new/$', views.local_new, name='new_local'),
    url(r'^local/(?P<locais_post_id>[0-9]+)/edit/$', views.local_edit, name='edit_local'),
    url(r'^local/(?P<locais_post_id>[0-9]+)/delete/$', views.local_delete, name='delete_local'),
    url(r'^login/$', views.user_logout, name='logout')
]

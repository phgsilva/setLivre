from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^projeto/(?P<id>[0-9]+)$', views.projeto, name='projeto'),
    url(r'^bio/(?P<id>[0-9]+)$', views.bio, name='bio'),
    url(r'^artigo/(?P<id>[0-9]+)$', views.artigo, name='artigo'),
]
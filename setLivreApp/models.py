from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Integrante(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    bio = models.TextField()
    caminho_foto = models.CharField(max_length=500)

    def salvar(self):
        self.save()

    def __unicode__(self):
        return self.nome 

class Projeto(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.TextField()

    def salvar(self):
        self.save() 

    def __unicode__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=150, blank=False, null=False)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField()
    caminho_foto = models.CharField(max_length=500)
    autor = models.ForeignKey('Integrante')
    projeto = models.ForeignKey('Projeto')

    def salvar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __unicode__(self):
        return self.titulo 

from django.contrib import admin
from .models import Artigo, Projeto, Integrante

# Register your models here.

admin.site.register(Artigo)
admin.site.register(Projeto)
admin.site.register(Integrante)


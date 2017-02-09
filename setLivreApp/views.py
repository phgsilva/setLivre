from django.shortcuts import render, get_object_or_404
from .models import Projeto, Artigo, Integrante

# Create your views here.

def index(request):
    return render(request, 'setLivreApp/index.html')

def contato(request):
    return render(request, 'setLivreApp/contato.html')

def sobre(request):
    return render(request, 'setLivreApp/sobre.html')

def projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, 'setLivreApp/projeto.html', {'projeto': projeto})

def artigo(request, id):
    return render(request, 'setLivreApp/artigo.html')

def bio(request, id):
    return render(request, 'setLivreApp/bio.html')

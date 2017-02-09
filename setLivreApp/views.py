from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'setLivreApp/index.html')

def contato(request):
    return render(request, 'setLivreApp/contato.html')

def sobre(request):
    return render(request, 'setLivreApp/sobre.html')

def projeto(request, id):
    return render(request, 'setLivreApp/projeto.html')

def artigo(request, id):
    return render(request, 'setLivreApp/artigo.html')

def bio(request, id):
    return render(request, 'setLivreApp/bio.html')

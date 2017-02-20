import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Projeto, Artigo, Integrante

# Create your views here.

def index(request):
    return render(request, 'setLivreApp/index.html')

def contato(request):
    return render(request, 'setLivreApp/contato.html')

def sobre(request):
    integrantes = Integrante.objects.all()
    return render(request, 'setLivreApp/sobre.html', {'integrantes': integrantes})

def projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    artigos = Artigo.objects.filter(projeto=projeto, 
                                    data_publicacao__year=datetime.date.today().year).order_by('data_publicacao')
    paginador = Paginator(artigos, 10)
    pagina = request.GET.get('pagina')

    try:
        pagina_artigos = paginador.page(pagina)
    except PageNotAnInteger:
        pagina_artigos = paginador.page(1)
    except EmptyPage:
        pagina_artigos = paginador.page(1)

    retorno = {'projeto': projeto,
                'artigos': pagina_artigos}

    return render(request, 'setLivreApp/projeto.html', {'valores': retorno})

def artigo(request, id):
    artigo = get_object_or_404(Artigo, pk=id)
    return render(request, 'setLivreApp/artigo.html', {'artigo': artigo})

def bio(request, id):
    bioagrafia = get_object_or_404(Integrante, pk=id)
    return render(request, 'setLivreApp/bio.html', {'bioagrafia': bioagrafia})

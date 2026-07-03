from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Artigo, Categoria

def home(request):
    noticias = Artigo.objects.all()
    categorias = Categoria.objects.all()
    
    contexto = {
        "lista_artigos": noticias,
        "lista_categorias": categorias
    }
    
    return render(request, 'blog/index.html', contexto)

def sobre_mim(request):
    return render(request, 'blog/sobre.html')
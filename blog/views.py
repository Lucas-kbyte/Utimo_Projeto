from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtigoSerializer

from .models import Artigo, Categoria
from .forms import ContatoForm

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

def artigo_detalhes(request, id):
    artigo = get_object_or_404(Artigo, pk=id)
    return render(request, 'blog/detalhes.html', {'artigo': artigo})

def fale_conosco(request):
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = ContatoForm()
        
    contexto = {
        "form": formulario
    }
        
    return render(request, 'blog/contato.html', {'formulario': formulario})

@api_view(['GET'])
def api_listar_artigo(request):
    artigos = Artigo.objects.all()
    
    serializer = ArtigoSerializer(artigos, many=True)
    
    return Response(serializer.data)
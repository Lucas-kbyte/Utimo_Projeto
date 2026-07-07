from django.contrib import admin
from .models import Categoria, Artigo, MensagemContato

admin.site.register(Categoria, MensagemContato)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'autor', 'data_publicacao', 'categoria')
    
    search_fields = ('titulo', 'conteudo')
    
    list_filter = ('categoria', 'data_publicacao')
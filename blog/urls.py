from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artigo/<int:id>', views.artigo_detalhes, name="detalhe_artigo"),
    
    # Adicione essa linha aqui embaixo:
    path('sobre/', views.sobre_mim, name='about'), 
]
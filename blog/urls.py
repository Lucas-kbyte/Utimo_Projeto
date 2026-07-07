from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artigo/<int:id>', views.artigo_detalhes, name="detalhe_artigo"),

    path('sobre/', views.sobre_mim, name='about'), 
    path('contato/', views.fale_conosco, name='contact')
    
    path('api/artigos/', views.api_listar_artigo, name='api_listar_artigo'),
]
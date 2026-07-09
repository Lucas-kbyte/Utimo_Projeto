from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('artigo/<int:id>/', views.artigo_detalhes, name="detalhe_artigo"),

    path('sobre/', views.sobre_mim, name='sobre'), 
    path('contato/', views.fale_conosco, name='contato'),
    
    # API endpoints
    path('api/artigos/', views.api_listar_artigo, name='api_listar_artigo'),
]
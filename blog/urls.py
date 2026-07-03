from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('artigo/<int:id>', views.arigo_detalhes, name="detalhe_artigo"),
]
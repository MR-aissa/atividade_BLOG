from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    Eu_lista = Eu.objects.all()
    detalhes = {
        'listagem': Eu_lista,
    }
    return render(request, 'blog/index.html', detalhes)

def sobre(request):
    Eu_lista = Eu.objects.all()
    detalhes = {
        'listagem': Eu_lista,
    }
    return render(request, 'blog/sobre.html', detalhes)

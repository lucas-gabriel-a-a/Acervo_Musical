from django.shortcuts import render
from django.http import HttpResponse
from .models import Artistas

# Create your views here.

def index(request):
    artistas = Artistas.objects.all()
    return render(request,'index.html',{'artistas':artistas})
    #return HttpResponse("Hallo Blumenau")

def ver_artista(request,id_artista):
    artista = Artistas.objects.filter(id=id_artista)
    return render(request,'index.html',{'artistas':artista})
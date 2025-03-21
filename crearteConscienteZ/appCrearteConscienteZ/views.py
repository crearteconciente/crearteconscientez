from contextlib import redirect_stderr
from django.shortcuts import render # type: ignore
# Create your views here.
def home (request):
    return render(request,"home.html")

def portalDeAcceso(request):
    return render(request, 'portalDeAcceso.html')

def ayuda(request):
    return render(request, 'ayuda.html')

def registroUsuario(request):
    return render(request, "registroUsuario.html") 

def elementos(request):
    return render(request, 'elementos.html')

def elemento_agua(request):
    return render(request, 'elemento_agua.html')

def elemento_tierra(request):
    return render(request, 'elemento_tierra.html')

def elemento_fuego(request):
    return render(request, 'elemento_fuego.html')

def elemento_aire(request):
    return render(request, 'elemento_aire.html')


def mision_tierra(request):
    return render(request, 'mision_tierra.html')
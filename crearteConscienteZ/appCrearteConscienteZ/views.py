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



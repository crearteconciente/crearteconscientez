"""
URL configuration for crearteConscieteZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore

from appCrearteConscienteZ import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appCrearteConscienteZ.urls')),
    path('', views.home, name='home'),
    path('portalDeAcceso/', views.portalDeAcceso, name='portalDeAcceso'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('elementos/', views.elementos, name='elementos'),
    path('portalDeAcceso/registroUsuario/', views.registroUsuario, name='registroUsuario'),
    path('elemento_agua/', views.elemento_agua, name='elemento_agua'),
    path('elemento_tierra/', views.elemento_tierra, name='elemento_tierra'),
    path('elemento_fuego/', views.elemento_fuego, name='elemento_fuego'),
    path('elemento_aire/', views.elemento_aire, name='elemento_aire'),

    path('mision-tierra/', views.mision_tierra, name='mision_tierra'),
]

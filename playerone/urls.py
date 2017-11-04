"""playerone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from web import views

urlpatterns = [
    #Admin
    url(r'^admin/', admin.site.urls),
    
    #Sistema
    url(r'^salir/', views.salir, name='salir'),
    url(r'^registrarse/', views.registrarse, name='registrarse'),
    url(r'^ingresar/', views.ingresar, name='ingresar'),
    url(r'^recuperar/', views.recuperar, name='recuperar'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^mi_perfil/', views.mi_perfil, name='mi_perfil'),
    url(r'^mi_perfil_ayuda/', views.mi_perfil_ayuda, name='mi_perfil_ayuda'),    
    url(r'^form_alta_cancha/', views.form_alta_cancha, name='form_alta_cancha'),
    url(r'^alta_reserva/', views.alta_reserva, name='alta_reserva'),
    url(r'^eliminar_reserva/', views.eliminar_reserva, name='eliminar_reserva'),
    url(r'^listado_canchas/', views.listado_canchas, name='listado_canchas'),
    url(r'^form_alta_complejo/', views.form_alta_complejo, name='form_alta_complejo'),
    url(r'^datos_complejo/', views.datos_complejo, name='datos_complejo'),
    url(r'^$', views.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
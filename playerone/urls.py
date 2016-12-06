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
    url(r'^registrarse/', views.registrarse, name='registrarse'),
    url(r'^ingresar/', views.ingresar, name='ingresar'),
    url(r'^recuperar/', views.recuperar, name='recuperar'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^form_alta_cancha/', views.form_alta_cancha, name='form_alta_cancha'),
    url(r'^form_alta_complejo/', views.form_alta_complejo, name='form_alta_complejo'),
    url(r'^$', views.index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
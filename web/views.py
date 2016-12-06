#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Usuario, Telefono, TelefonosUsuario, TipoTelefono, TipoUsuario, Cancha, Complejo
import json


def index(request):
    mensaje = 'INDEX'
    
    context = {'mensaje': mensaje,}
    return render(request, 'index.html', context)

def recuperar(request):

    dict = {'error': '', 'result': ''}

    email = request.POST.get('email')

    try:
        usuario = User.objects.get(username=email) 
        error = ''
        result = 'Se le envio el nuevo password (no olvides revisar el spam).'
    except ObjectDoesNotExist:
        error = 'Usuario inexistente!'
        result = ''
    
    dict = {'error': error, 'result': result}

    return HttpResponse(json.dumps(dict), content_type="application/json")

def ingresar(request):
    mensaje = ''
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':

        username = request.POST.get('email')
        password = request.POST.get('password')
        
        if username == '' or password == '':
            mensaje = 'Ambos campos son obligatorios.'
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('dashboard'))
                else:
                    mensaje = 'La cuenta esta inactiva. Comuniquese con el administrador.'
            else:        
                mensaje = 'Nombre de usuario o contraseña no valido.'
    
    
    context = {'mensaje': mensaje,}
    return render(request, 'ingresar.html', context)

def registrarse(request):
    mensaje = ''
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            nombre      = request.POST.get('nombre')
            apellido    = request.POST.get('apellido')
            telefonotxt = request.POST.get('telefono')
            email       = request.POST.get('email')
            password    = request.POST.get('password')
            repassword  = request.POST.get('password_confirmation')

            users = User.objects.filter(email=email)
            
            if len(users) > 0:
                mensaje = "Ya existe el email con el que desea registrarse."
                dict = {'error': mensaje}
                return HttpResponse(json.dumps(dict), content_type="application/json")
            else:
                user = User.objects.create_user(email, email, password)
                user.first_name = nombre
                user.last_name  = apellido
                user.is_staff = False
                user.save()

                usuario = Usuario()
                usuario.user = user
                usuario.tipo_usuario = TipoUsuario.objects.get(nombre = 'Trial')
                usuario.save()
                
                telefono = Telefono()
                telefono.telefono = telefonotxt
                telefono.tipoTelefono = TipoTelefono.objects.get(nombre = 'Particular')
                telefono.comentario = 'Telefono ingresado en el proceso de registro.'
                telefono.save()
                            
                teleUsuario  = TelefonosUsuario()
                teleUsuario.usuario = usuario
                teleUsuario.telefono = telefono
                teleUsuario.save()

        except Exception as e:
            mensaje = str(e)
            
        dict = {'error': mensaje}
        return HttpResponse(json.dumps(dict), content_type="application/json")
            
    context = {'mensaje': mensaje,}
    return render(request, 'registrarse.html', context)            
    
def dashboard(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)
    complejo_sel = complejos[0]
    canchas_complejo = complejo_sel.cancha_set.all()

    context = {'mensaje': mensaje, 'complejos': complejos, 'canchas_complejo':canchas_complejo, 'complejo_sel':complejo_sel}
    return render(request, 'dashboard.html', context)
    

def form_alta_cancha(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'form-alta-cancha.html', context)

def form_alta_complejo(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'form-alta-complejo.html', context)
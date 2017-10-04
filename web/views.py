#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.template.defaulttags import register
from django.http import HttpResponse
from django.utils.translation import ugettext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Usuario, Telefono, TelefonosUsuario, TipoTelefono, TipoUsuario, Cancha, Complejo, Reserva, UsuariosComplejos
import json
import datetime

def index(request):
    mensaje = 'INDEX'
    
    context = {'mensaje': mensaje,}
    return render(request, 'index.html', context)

def salir(request):
    mensaje = ''
    logout(request)
    return redirect(reverse('ingresar'))

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
        if request.user.is_authenticated():
            return redirect(reverse('dashboard'))
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
                mensaje = 'Nombre de usuario o password no valido.'
    
        print mensaje
    
    context = {'mensaje': mensaje,}
    return render(request, 'ingresar.html', context)

def registrarse(request):
    mensaje = ''
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            nombre      = request.POST.get('fullname')
            email       = request.POST.get('email')
            telefono_n  = request.POST.get('telefono')
            complejo_n  = request.POST.get('complejo')
            password    = request.POST.get('password')
            rpassword   = request.POST.get('rpassword')

            users = User.objects.filter(email=email)
            
            if len(users) > 0:
                mensaje = "Ya existe el email con el que desea registrarse."
            else:
                user = User.objects.create_user(email, email, password)
                user.first_name = nombre
                user.is_staff = False
                user.save()

                usuario = Usuario()
                usuario.user = user
                usuario.tipo_usuario = TipoUsuario.objects.get(nombre = 'Administrador')
                usuario.save()
                
                telefono = Telefono()
                telefono.telefono = telefono_n
                telefono.tipoTelefono = TipoTelefono.objects.get(nombre = 'Particular')
                telefono.comentario = 'Telefono ingresado en el proceso de registro.'
                telefono.save()
                            
                teleUsuario  = TelefonosUsuario()
                teleUsuario.usuario = usuario
                teleUsuario.telefono = telefono
                teleUsuario.save()

                complejo = Complejo()
                complejo.nombre = complejo_n
                complejo.direccion = 'Direccion complejo'
                complejo.save()

                usu_compl = UsuariosComplejos()
                usu_compl.complejo = complejo
                usu_compl.usuario = usuario
                usu_compl.save()

                return redirect(reverse('dashboard'))

        except Exception as e:
            mensaje = str(e)
            
    context = {'mensaje_nuevo': mensaje,}
    return render(request, 'ingresar    .html', context)            
    
@login_required
def dashboard(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)
    complejo_sel = complejos[0]
    canchas_complejo = complejo_sel.cancha_set.all()

    import datetime
    fecha = datetime.date.today().strftime("%d/%m/%Y")

    lista_horarios_text = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '00:00', '00:30']
    lista_horarios = ['1000', '1030', '1100', '1130', '1200', '1230', '1300', '1330', '1400', '1430', '1500', '1530', '1600', '1630', '1700', '1730', '1800', '1830', '1900', '1930', '2000', '2030', '2100', '2130', '2200', '2230', '2300', '2330', '0000', '0030']
    dict_horarios = {}
    tabla = []
    
    for hora in lista_horarios:
        
        dict_horarios = {}
        dict_horarios['horario'] = hora[:2] + ':' + hora[2:]
        
        fecha_inicio = datetime.datetime.now().strftime ("%Y%m%d")
        fecha_inicio = fecha_inicio + hora
        
        for cancha in canchas_complejo:
            reservas = Reserva.objects.filter(cancha=cancha, fecha_inicio=fecha_inicio)
            if reservas:
                dict_horarios[cancha.nombre] = 'reservada'
            else:
                dict_horarios[cancha.nombre] = 'libre'
        tabla.append(dict_horarios)
    ancho = 95 / len(canchas_complejo)    
    
    context = {'fecha': fecha,'mensaje': mensaje, 'complejos': complejos, 'canchas_complejo':canchas_complejo, 'complejo_sel':complejo_sel, 'tabla':tabla, 'lista_horarios_text': lista_horarios_text, 'ancho':ancho}
    return render(request, 'dashboard.html', context)
    
@login_required
def form_alta_cancha(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'form-alta-cancha.html', context)

@login_required
def listado_canchas(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)
    complejo_sel = complejos[0]
    canchas_complejo = complejo_sel.cancha_set.all()

    context = {'mensaje': mensaje, 'complejos': complejos,'canchas_complejo':canchas_complejo, 'complejo_sel':complejo_sel, }
    return render(request, 'listado-canchas.html', context)

@login_required
def form_alta_complejo(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'form-alta-complejo.html', context)

@login_required
def datos_complejo(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)
    complejo_sel = complejos[0]

    context = {'mensaje': mensaje, 'complejos': complejos, 'complejo_sel':complejo_sel, }
    return render(request, 'datos-complejo.html', context)

@login_required
def mi_perfil(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'mi-perfil.html', context)

@login_required
def mi_perfil_ayuda(request):
    mensaje = 'INDEX'
    complejos = Complejo.objects.filter(usuarioscomplejos__usuario__user__username=request.user.username)

    context = {'mensaje': mensaje, 'complejos': complejos, }
    return render(request, 'mi-perfil-ayuda.html', context)
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

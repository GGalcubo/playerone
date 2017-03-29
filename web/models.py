#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode


class Deporte(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Deportes" 

class Superficie(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Superficies" 
		
class TipoReserva(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Reserva"

class TipoTelefono(models.Model):	
    nombre = models.CharField('Nombre', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Telefono"
        
class TipoUsuario(models.Model):		
    nombre = models.CharField('Nombre', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)
    es_admin = models.BooleanField('Es Administrador', default=False)
    es_usuario = models.BooleanField('Es Usuario', default=False)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Usuario"

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(TipoUsuario, null=True, blank=True)
    fecha_creacion = models.CharField('Fecha creacion', default='000000000000', max_length=12)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Usuarios" 
        
class Telefono(models.Model):
    telefono = models.CharField('Telefono', max_length=250)
    comentario = models.TextField('Comentario', null=True, blank=True)
    tipoTelefono = models.ForeignKey(TipoTelefono, null=True, blank=True)

    def __str__(self):
        return self.telefono

    class Meta:
        verbose_name_plural = "Telefonos" 
        
class Complejo(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    facebook = models.CharField('Facebook', max_length=250, null=True, blank=True)
    twitter = models.CharField('Twitter', max_length=250, null=True, blank=True)
    direccion = models.CharField('Direccion', max_length=250)
    patrocinador = models.CharField('Patrocinador', max_length=250, null=True, blank=True)
    #horario
    comentario = models.TextField('Comentario', null=True, blank=True)
    vestuarios = models.BooleanField('Vestuarios', default=False)
    duchas = models.BooleanField('Duchas', default=False)
    bar = models.BooleanField('Bar', default=False)
    restaurant = models.BooleanField('Restaurant', default=False)
    parrilla = models.BooleanField('Parrilla', default=False)
    wifi = models.BooleanField('Wifi', default=False)
    tv = models.BooleanField('TV', default=False)
    seguridad = models.BooleanField('Seguridad', default=False)
    estacionamiento = models.BooleanField('Estacionamiento', default=False)
    tarjetas = models.BooleanField('Tarjeta Debito/Credito', default=False)
    festejos = models.BooleanField('Festejos', default=False)
    escuelita = models.BooleanField('Escuelita', default=False)
    torneos = models.BooleanField('Torneos', default=False)
    colegios = models.BooleanField('Colegios', default=False)

    def tiene_vestuarios(self):
           if self.vestuarios:
               return 'checked'
           else:
               return ''

    def tiene_duchas(self):
           if self.duchas:
               return 'checked'
           else:
               return ''

    def tiene_bar(self):
           if self.bar:
               return 'checked'
           else:
               return ''

    def tiene_restaurant(self):
           if self.restaurant:
               return 'checked'
           else:
               return ''

    def tiene_parrilla(self):
           if self.parrilla:
               return 'checked'
           else:
               return ''

    def tiene_wifi(self):
           if self.wifi:
               return 'checked'
           else:
               return ''

    def tiene_tv(self):
           if self.tv:
               return 'checked'
           else:
               return ''

    def tiene_seguridad(self):
           if self.seguridad:
               return 'checked'
           else:
               return ''

    def tiene_estacionamiento(self):
           if self.estacionamiento:
               return 'checked'
           else:
               return ''

    def tiene_tarjetas(self):
           if self.tarjetas:
               return 'checked'
           else:
               return ''

    def tiene_festejos(self):
           if self.festejos:
               return 'checked'
           else:
               return ''

    def tiene_escuelita(self):
           if self.escuelita:
               return 'checked'
           else:
               return ''

    def tiene_torneos(self):
           if self.torneos:
               return 'checked'
           else:
               return ''

    def tiene_colegios(self):
           if self.colegios:
               return 'checked'
           else:
               return ''

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Complejos" 

class Cancha(models.Model):
    nombre = models.CharField('Nombre', max_length=250)
    superficie = models.ForeignKey(Superficie, null=True, blank=True)
    deporte = models.ForeignKey(Deporte, null=True, blank=True)
    cant_jugadores = models.CharField('Cantidad Jugadores', max_length=50)
    precio = models.CharField('Precio', max_length=10)
    complejo = models.ForeignKey(Complejo, null=True, blank=True)
    techada = models.BooleanField('Techada', default=False)
    luz = models.BooleanField('Luz', default=False)

    def es_techada(self):
       if self.techada:
           return 'Techada'
       else:
           return ' '

    def tiene_luz(self):
       if self.luz:
           return 'Luz'
       else:
           return ' '

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Canchas" 

class Reserva(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    telefono = models.CharField('Telefono', max_length=15)
    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    cancha = models.ForeignKey(Cancha, null=True, blank=True)
    tipo_reserva = models.ForeignKey(TipoReserva, null=True, blank=True)
    fecha_inicio = models.CharField('Fecha Inicio', default='000000000000', max_length=12)
    fecha_fin = models.CharField('Fecha Fin', default='000000000000', max_length=12)
    precio = models.CharField('Precio', max_length=10)
    sena = models.CharField('Senia', max_length=10)
    pago = models.CharField('Pago', max_length=10)
    evento = models.BooleanField('Evento', default=False)
    actualizado_por = models.ForeignKey(Usuario, null=True, blank=True,related_name = 'actualizado_por')
    fecha_cracion = models.CharField('Fecha creacion', default='000000000000', max_length=12)
    fecha_atualizacion = models.CharField('Fecha Actualizacion', default='000000000000', max_length=12)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Reservas"
    
class Reputacion(models.Model):
    reputacion = models.CharField('Reputacion', max_length=10)
    comentario = models.TextField('Comentario', null=True, blank=True)
    fecha = models.CharField('Fecha', default='00000000', max_length=8)

    def __str__(self):
        return self.reputacion

    class Meta:
        verbose_name_plural = "Reputacion"

class ReputacionComplejo(models.Model):
    complejo = models.ForeignKey(Complejo)
    reputacion = models.ForeignKey(Reputacion)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.complejo

    class Meta:
        verbose_name_plural = "Reputaciones Complejo"
        
class ReputacionUsuario(models.Model):
    usuario = models.ForeignKey(Usuario)
    reputacion = models.ForeignKey(Reputacion)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name_plural = "Reputaciones Usuario"
        
class TelefonosComplejo(models.Model):
    complejo = models.ForeignKey(Complejo)
    telefono = models.ForeignKey(Telefono)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.complejo.nombre

    class Meta:
        verbose_name_plural = "Telefonos Complejo"
        
class TelefonosUsuario(models.Model):
    usuario = models.ForeignKey(Usuario)
    telefono = models.ForeignKey(Telefono)
    comentario = models.TextField('Comentario', null=True, blank=True)

    def __str__(self):
        return self.usuario.user.username

    class Meta:
        verbose_name_plural = "Telefonos Usuario" 
        
class ImagenesCanchas(models.Model):
    cancha = models.ForeignKey(Cancha)
    imagen = models.ImageField(upload_to="canchas/")
    nombre = models.CharField('Nombre', max_length=250, null=True, blank=True)
    comentario = models.TextField('Comentario', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Imagenes Cancha" 

class ImagenesComplejos(models.Model):
    complejo = models.ForeignKey(Complejo)
    imagen = models.ImageField(upload_to="complejos/")
    nombre = models.CharField('Nombre', max_length=250, null=True, blank=True)
    comentario = models.TextField('Comentario', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Imagenes Complejo"

class UsuariosComplejos(models.Model):
    complejo = models.ForeignKey(Complejo)
    usuario = models.ForeignKey(Usuario)
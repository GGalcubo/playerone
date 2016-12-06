from django.contrib import admin
from .models import Deporte, Superficie, TipoReserva, TipoUsuario, TipoTelefono, Usuario, Telefono, Complejo, Cancha, Reserva, Reputacion, ReputacionComplejo, ReputacionUsuario, TelefonosComplejo, TelefonosUsuario, ImagenesCanchas, ImagenesComplejos, UsuariosComplejos

class UsuariosComplejosInline(admin.TabularInline):
    model = UsuariosComplejos
    extra = 0
    
class TelefonosComplejoInline(admin.TabularInline):
    model = TelefonosComplejo
    extra = 0
    
class TelefonosUsuarioInline(admin.TabularInline):
    model = TelefonosUsuario
    extra = 0

class ReputacionComplejoInline(admin.TabularInline):
    model = ReputacionComplejo
    extra = 0
    
class ReputacionUsuarioInline(admin.TabularInline):
    model = ReputacionUsuario
    extra = 0
    
class ImagenesCanchasInline(admin.TabularInline):
    model = ImagenesCanchas
    extra = 0

class ImagenesComplejosInline(admin.TabularInline):
    model = ImagenesComplejos
    extra = 0

class CanchaInline(admin.TabularInline):
    model = Cancha
    extra = 0

class CanchaAdmin(admin.ModelAdmin):
    inlines = [
        ImagenesCanchasInline
    ]
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ['nombre', 'superficie', 'deporte', 'cant_jugadores', 'precio', 'complejo', 'techada', 'luz']
        }),
    )
    
class UsuarioAdmin(admin.ModelAdmin):
    inlines = [
        TelefonosUsuarioInline
    ]
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ['user', 'tipo_usuario', 'fecha_creacion']
        }),
    )

class ComplejoAdmin(admin.ModelAdmin):
    inlines = [
        CanchaInline, ImagenesComplejosInline, TelefonosComplejoInline, ReputacionComplejoInline, UsuariosComplejosInline
    ]
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ['nombre', 'facebook', 'twitter', 'direccion', 'patrocinador', 'comentario']
        }),
        ('Extras', {
            'fields': ['vestuarios', 'duchas', 'bar', 'restaurant', 'parrilla', 'wifi', 'tv', 'seguridad', 'estacionamiento', 'tarjetas', 'festejos', 'escuelita', 'torneos', 'colegios']
        }),
    )


admin.site.register(TelefonosUsuario)  
admin.site.register(UsuariosComplejos)    
admin.site.register(TipoTelefono)
admin.site.register(TipoReserva)
admin.site.register(TipoUsuario)
admin.site.register(Reputacion)
admin.site.register(Reserva)
admin.site.register(Deporte)
admin.site.register(Superficie)
admin.site.register(Telefono)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Complejo, ComplejoAdmin)
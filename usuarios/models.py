from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Roles  # Importa el modelo Roles


class Usuario(AbstractUser):
    rol = models.ForeignKey(Roles, models.SET_NULL, null=True, blank=True, verbose_name="Rol")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_sesion = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'usuarios_usuario' # Corregido aquí
        verbose_name = "Usuario del Sistema"     #define un nombre legible para el modelo cuando se muestra en el Django Admin o en otros lugares donde se hace referencia al modelo.
        verbose_name_plural = "Usuarios del Sistema" #define un nombre legible para el modelo cuando se muestra en el Django Admin o en otros lugares donde se hace referencia al modelo.

    def __str__(self):
        return self.username

class IntentosFallidos(models.Model):
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    ip_usuario = models.CharField(max_length=50, blank=True, null=True)
    fecha_intento = models.DateTimeField()

    class Meta:
        db_table = 'intentos_fallidos'
        db_table_comment = 'Esta tabla registra los intentos fallidos de login para un usuario específico.'
        verbose_name = "Intento Fallido"
        verbose_name_plural = "Intentos Fallidos"
        

class Sesiones(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    token_sesion = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    ip_usuario = models.CharField(max_length=50, blank=True, null=True)
    agente_usuario = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sesiones'
        db_table_comment = 'Esta tabla almacena las sesiones activas de los usuarios, incluyendo tokens de sesión, IP y agente del usuario.'
        verbose_name = "Sesión"   
        verbose_name_plural = "Sesiones"
        
class CambioContrasena(models.Model):
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    fecha_cambio = models.DateTimeField()
    ip_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'cambio_contrasena'
        db_table_comment = 'Esta tabla registra los cambios de contraseñas realizados por los usuarios.'
        verbose_name = 'Cambio de contraseña'
        verbose_name_plural = 'Cambios de contraseñas'
       
from django.db import models
from usuarios.models import Usuario

class RegistroAcciones(models.Model):
    id_log = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    accion = models.CharField(max_length=255, blank=True, null=True)
    fecha_accion = models.DateTimeField()
    ip_usuario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'registro_acciones'
        db_table_comment = 'Esta tabla almacena un historial de las acciones realizadas por los usuarios, como accesos y cambios importantes.'
        verbose_name = 'Registro de Accion'
        verbose_name_plural = 'Registros de Acciones'
        
class Auditoria(models.Model):
    id_log = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.SET_NULL, null=True, blank=True, verbose_name="Usuario")
    accion = models.CharField(max_length=255, verbose_name="Acción")
    fecha_accion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Acción")
    ip_usuario = models.CharField(max_length=50, blank=True, null=True, verbose_name="IP del Usuario")
    objeto_afectado = models.TextField(blank=True, null=True, verbose_name="Objeto Afectado")

    class Meta:
        db_table = 'auditoria'
        verbose_name = 'Registro de Auditoría'
        verbose_name_plural = 'Registros de Auditorías'
        ordering = ['-fecha_accion']
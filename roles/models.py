from django.db import models
# Create your models here.

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion_rol = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'roles'
        db_table_comment = 'Esta tabla almacena los roles disponibles en el sistema, como admin, usuario, etc.'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        

    def __str__(self):
        return self.nombre_rol



from django.contrib import admin
from .models import Usuario, IntentosFallidos, Sesiones, CambioContrasena

admin.site.register(Usuario)
admin.site.register(IntentosFallidos)
admin.site.register(Sesiones)
admin.site.register(CambioContrasena)
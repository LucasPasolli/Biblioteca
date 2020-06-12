from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    #fields = ('codigo', 'telefono')

    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre', 'direccion', 'telefono')
        }),
        ('Detalle de alquileres', {
            'fields': ('ejemplares',)
        }),
    )
    list_display = ['nombre', 'telefono', 'direccion']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Autor)

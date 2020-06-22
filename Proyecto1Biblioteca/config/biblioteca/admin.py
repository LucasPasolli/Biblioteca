from django.contrib import admin
from .models import *

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['libro', 'codigo', 'localizacion']
    list_display_links = ('codigo', 'localizacion', 'libro')
    search_fields = ['libro__titulo']

class UsuarioAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Datos',{
            'fields': ('nombre',)
            
        }),
        ('Contacto', {
            'fields': ('telefono', 'direccion',)
        }),
    )
    #list_display = ['nombre', 'telefono', 'direccion']

class EntryAdmin(admin.ModelAdmin):
    list_display = ('get_nombre', 'title', 'content')
    list_display_links = ('get_nombre', 'title')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial')
    
class LibroInline(admin.TabularInline):
    model = Libro
    fields = ['titulo', 'editorial', 'paginas']

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    list_display_links = ('nombre',)
    search_fields = ['nombre']
    inlines = [LibroInline]
    

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Entry, EntryAdmin)

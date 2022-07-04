from django.contrib import admin
from .models import Curso

# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'calificacion')
    search_fields = ('nombre', 'calificacion')
    # list_editable = ('nombre',)
    list_display_links = ('nombre',)
    list_filter = ('calificacion',)
    
    fieldsets = (
        (None, {
            'fields':('nombre',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('calificacion', )
        })  
    )
    
    # def datos(self, obj):
    #     return obj.nombre.upper()
        
import csv
from django.contrib import admin
from django.db.models import Count
from django.http import HttpResponse

from .models import Category, Origin, Hero, Villain
from events.admin import event_admin_site
from mixin.admin_mixin import ExportCsvMixin

# Register your models here.

event_admin_site.register(Category)


class OriginAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "hero_count", "villain_count")
    actions = ['export_as_csv']

    """
    Si tienes muchos campos calculados en tu administrador
    Puedes estar ejecutando múltiples consultas y 
    tu administrador se hará lento
    Para corregir esto: sobreescribe el metodo get_queryset
    """ 
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count

    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'


event_admin_site.register(Origin, OriginAdmin)


class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    """
    Personalización del model Hero en el admin
    """
    # La funcion puede mostrar un campo calculado en el admin
    # pero este campo no se puede añadir a filtros
    def is_very_benevolent(self, obj):
        return obj.benevolence_factor > 7

    def mark_immortal(self, request, queryset):
        self.message_user(request, "All heroes are now immortal")
        queryset.update(is_inmortal=True)
    
    def mark_mortal(self, request, queryset):
        self.message_user(request, "All heroes are now mortals")
        queryset.update(is_inmortal=False)


    class IsVeryBenevolentFilter(admin.SimpleListFilter):
        """
        para añadir un campo calculado a los filtros
        debemos sobreescribir la subclase SimpleListFilter 

        """
        title = 'is_very_benevolent'
        parameter_name = 'is_very_benevolent'
      
        def lookups(self, request, model_admin):
            return (
                ('Yes', True),
                ('No', False),
            ) 
     
        def queryset(self, request, queryset):
            value = self.value()
            if value == True:
                return queryset.filter(benevolence_factor__gt=7)
            elif value == False:
                return queryset.exclude(benevolence_factor__gt=7)
            return queryset
    
    
    # muestra los campos en el admin, incluyendo el campo calculado que creamos
    list_display = ("name", "is_inmortal", "category", "origin", "is_very_benevolent",)
    # permite estos filtros en el panel, incluyendo el filtro q creamos
    list_filter = ("is_inmortal", "category", "origin", IsVeryBenevolentFilter)
    # listado de acciones 
    actions = ["mark_immortal", "mark_mortal", "export_as_csv"]

    # esta variable es para mostrar icono de off/on
    is_very_benevolent.boolean = True

    # cambiar el nombre de las acciones
    mark_immortal.short_description = "Make me a Immortal"
    mark_mortal.short_description = "Make me a Mortal"

event_admin_site.register(Hero, HeroAdmin)


class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "is_immortal", "category", "origin", "is_very_malevolence", )
    actions = ['export_as_csv']

    def is_very_malevolence(self, obj):
        return obj.malevolence_factor > 7
    
    is_very_malevolence.boolean = True

    # malevolence_factor
    # power_factor

event_admin_site.register(Villain, VillainAdmin)
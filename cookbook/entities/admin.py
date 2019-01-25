from django.contrib import admin
from .models import Category, Origin, Hero, Villain

from events.admin import event_admin_site
# Register your models here.

event_admin_site.register(Category)
event_admin_site.register(Hero)
event_admin_site.register(Villain)

#@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", "hero_count", "villain_count")

    """
    Si tienes muchos campos calculados en tu administrador
    Puedes estar ejecutando múltiples consultas y 
    tu administrador se hará lento
    Para corregir esto: sobreescribe el metodo get_queryset
    """ 

    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villain_set.count()


event_admin_site.register(Origin, OriginAdmin)
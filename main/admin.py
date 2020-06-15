from django.contrib import admin
from main.models import Soja, Milho, Cafe

# Register your models here.


class SojaAdmin(admin.ModelAdmin):
    list_display = ['data', 'cotacao', 'variacao']


class MilhoAdmin(admin.ModelAdmin):
    list_display = ['data', 'cotacao', 'variacao']


class CafeAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'data', 'cotacao', 'variacao']


admin.site.register(Soja, SojaAdmin)
admin.site.register(Milho, MilhoAdmin)
admin.site.register(Cafe, CafeAdmin)

from django.contrib import admin
from .models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_evento', 'usuario']
    list_filter = ['data_evento', 'usuario']

admin.site.register(Evento, EventoAdmin)
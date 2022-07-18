from django.contrib import admin

from .models import Bus, Chofer, Pasajero, Trayecto

# Register your models here.
admin.site.register(Bus)
admin.site.register(Chofer)
admin.site.register(Pasajero)
admin.site.register(Trayecto)

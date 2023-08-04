from django.contrib import admin

# Register your models here.

from .models import Canchas
from .models import Reserva
from .models import Gestion 

admin.site.register(Canchas)
admin.site.register(Reserva)
admin.site.register(Gestion)
from django.contrib import admin
from .models import Hotels,Rooms,Reservation,Equipment,Equip_Reservation
# Register your models here.
admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Equipment)
admin.site.register(Equip_Reservation)
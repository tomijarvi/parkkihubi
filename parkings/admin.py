from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Address, Operator, Parking, ParkingArea


class AddressAdmin(admin.ModelAdmin):
    pass


class OperatorAdmin(admin.ModelAdmin):
    pass


class ParkingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Parking, ParkingAdmin)
admin.site.register(ParkingArea, OSMGeoAdmin)

# -*- coding: utf-8 -*-
from parking.models import User
from parking.models import ParkingLot
from parking.models import ParkingLotExtra
from parking.models import ParkingLotSpace
from parking.models import ParkingRecord
from parking.models import Offers
from parking.models import UserLog

from django.contrib import admin

#from utils import DecadeBornListFilter


admin.site.register(User)
admin.site.register(ParkingLotSpace)
admin.site.register(ParkingRecord)
admin.site.register(Offers)
admin.site.register(UserLog)


class ParkingLotExtraInline(admin.StackedInline):
    model = ParkingLotExtra
    fields = ['status', 'price']
    max_num = 1

class ParkingLotExtraAdmin(admin.ModelAdmin):
    fields = ['status', 'admin']

class ParkingLotAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'type', 'latitude', 'longitude']
    list_display = ('name', 'parking_lot_type_str', 'create_time',)
    #list_filter = [DecadeBornListFilter]
    search_fields = ['name']
    date_hierarchy = 'create_time'
    inlines = [ParkingLotExtraInline]



admin.site.register(ParkingLot, ParkingLotAdmin)







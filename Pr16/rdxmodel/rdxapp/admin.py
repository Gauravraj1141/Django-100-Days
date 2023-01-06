from django.contrib import admin
from .models import Trade1, Trade2


@admin.register(Trade1)
class Trade1Admin(admin.ModelAdmin):
    list_display = ['usname', "price", "stockname"]


@admin.register(Trade2)
class Trade2Admin(admin.ModelAdmin):
    list_display = ['oldtradename', 'newtradeprice', 'nameofnewtrade', ]

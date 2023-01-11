from django.contrib import admin

from .models import Locker


@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password', )

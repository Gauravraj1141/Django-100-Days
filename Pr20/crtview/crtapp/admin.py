from django.contrib import admin

from .models import ZoneSchools


@admin.register(ZoneSchools)
class ZoneSchoolsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'Contact_no', )

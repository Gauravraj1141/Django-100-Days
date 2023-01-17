from django.contrib import admin

from .models import PropertyDetail, City, State


@admin.register(PropertyDetail)
class Property_detailAdmin(admin.ModelAdmin):
    list_display = ('Pr_id', 'Property_name',
                    'Property_address', 'City_name',)


@admin.register(City)
class cityAdmin(admin.ModelAdmin):
    list_display = ('ct_id', 'ctname', 'state', )


@admin.register(State)
class stateAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'stname', )

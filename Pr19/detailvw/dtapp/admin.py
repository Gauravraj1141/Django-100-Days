from django.contrib import admin

from .models import mystudents


@admin.register(mystudents)
class mystudentsAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'name', 'clsname', 'marks', 'address', )

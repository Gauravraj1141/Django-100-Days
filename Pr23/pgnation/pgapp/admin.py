from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('blg_id', 'blg_name', 'blg_status', )

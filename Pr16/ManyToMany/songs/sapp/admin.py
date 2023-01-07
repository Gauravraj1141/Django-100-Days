from django.contrib import admin
from .models import MusicPlayer
# Register your models here.


@admin.register(MusicPlayer)
class MusicPlayerAdmin(admin.ModelAdmin):
    list_display = ('Song_id', 'Song_name', 'Song_duration', 'sing_by')

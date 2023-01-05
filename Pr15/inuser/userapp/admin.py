from django.contrib import admin
from .models import father, daughter, son, User, userproxy
# Register your models here.


@admin.register(father)
class fatherAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "profession")


@admin.register(daughter)
class daughterAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "profession", "age")


@admin.register(son)
class sonAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "profession", "age")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "age")


@admin.register(userproxy)
class userproxyAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "age")

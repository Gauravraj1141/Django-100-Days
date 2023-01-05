from django.contrib import admin
from .models import User, myuser, myuser_proxy


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'marks', )


@admin.register(myuser)
class myuserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'marks', )


@admin.register(myuser_proxy)
class myuser_proxyAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'marks', )

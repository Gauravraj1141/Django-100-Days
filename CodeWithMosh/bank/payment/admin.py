from django.contrib import admin

# Register your models here.
from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'upi_id', 'account_balance', ) 
    


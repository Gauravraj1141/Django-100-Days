from django.contrib import admin
from .models import Students, Teacher, Peon
# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('roll', 'Clsname', 'name', 'Address', 'Phone',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'Address', 'Phone', 'Salary', 'subject')


@admin.register(Peon)
class PeonAdmin(admin.ModelAdmin):
    list_display = ('name', 'Address', 'Phone', 'Salary',)

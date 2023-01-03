from django.contrib import admin
from .models import students, teacher
# Register your models here


@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'roll', 'Address', )


@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Salary', 'Dob', )

from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Students, Teacher, Peon


def home(request):
    data = Students.objects.all()
    for d in data:
        students = d
    data2 = Teacher.objects.all()
    for d in data2:
        teacher = d
    data3 = Peon.objects.all()
    for d in data3:
        peon = d
    return HttpResponse(f"students : {students.name},class {students.Clsname}  ,\n teacher: {teacher}, Peon: {peon}")

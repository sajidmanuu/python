from django.shortcuts import render, redirect
from .models import Student

def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        student = Student(name=name, email=email, age=age, gender=gender)
        student.save()
    return redirect('index')


def updateData(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.save()
        return redirect('index')
    context = {"d": student}
    return render(request, "update.html", context)

def deleteData(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('index')

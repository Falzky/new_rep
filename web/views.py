from django.shortcuts import render, redirect
from web.models import Student
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "app/index.html")

def hello(request, name):
    context={"name",name}
    return render(request, "app/hello.html", context)

def stud(request):
    all_students= Student.objects.all()
    for record in all_students:
        context={"data": all_students}
    return render(request, "app/student.html", context)

def newstud(request):
    if request.method =='POST':
        name= request.POST.get("fifth")
        age= request.POST.get("fourth")
        cgpa= request.POST.get("seven")
        d_o_b= request.POST.get("first")
        reg_number= request.POST.get("second")
        if not name or not reg_number or not d_o_b or not age or not cgpa:
            messages.error(request, "All fields are required")
            return redirect(newstudent)
            new_student= Student.objects.create(name= name, age= age, cgpa= cgpa, reg_number= reg_number)
            new_student.save()
            messages.success(request, "created successfully")
    return render(request, "app/new_student.html")

    def school(request):
        return render(request, app/hello.html)
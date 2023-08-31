from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from ScreenApp.models import Teacher,Identity,Department

def home(request):
    teacher1 = Teacher(name = 'momoi',
                       identity = Identity.教授,
                       department = Department.数字媒体系)
    teacherStr = teacher1.__str__
    print(teacherStr)
    return render(request,'home.html',{"teacherStr":teacherStr})


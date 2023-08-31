from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from ScreenApp.models import Teacher,Identity,Department

def home(request):
    teacher1 = Teacher(name = 'momoi',
                       identity = "教授",
                       department = "数字媒体系")
    return render(request,'home.html',{"teacher1":teacher1})


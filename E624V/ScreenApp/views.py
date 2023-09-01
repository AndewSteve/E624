from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from ScreenApp.models import Teacher,Identity,Department

def home(request):
    return render(request,'home.html',{})

def search(request):
    return render(request,'search.html',{})

def result(request):
    teacher1 = Teacher(name = '周博',
                       identity = "讲师",
                       department = "数字媒体系")
    teacher2 = Teacher(name = '符强',
                    identity = "副教授",
                    department = "数字媒体系")
    teacher3 = Teacher(name = '谭剑',
                    identity = "副教授",
                    department = "设计系")
    teacher4 = Teacher(name = '李霞',
                    identity = "教授",
                    department = "艺术教研中心")
    teachers = [teacher1,teacher2,teacher3,teacher4]
    return render(request,'result.html',{"teachers":teachers})




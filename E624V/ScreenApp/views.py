from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from ScreenApp.models import Teacher,Identity,Department

identities = Identity
departments = Department
def home(request):
    return render(request,'home.html',{"identities":identities,
                                       "departments":departments})

def result(request):
    if request.method == 'POST':
        teachers = Teacher.objects.all()
        teacher_name = request.POST.getlist('teacher_name')[0]
        teacher_identity_filter = request.POST.getlist('identity')
        teacher_department_filter = request.POST.getlist('department')
        
        if teacher_name:
            teachers = teachers.filter(name__contains = teacher_name)
        if teacher_identity_filter:
            teachers = teachers.filter(identity__in = teacher_identity_filter)
        if teacher_department_filter:
            teachers = teachers.filter(department__in = teacher_department_filter)

        return render(request,'result.html',{"teachers":teachers,
                                             "identities":identities,
                                             "departments":departments})
    else:
        notfound = "请在搜索框中输入教师名字关键字,或在左侧下拉菜单中选择添加筛选条件查询"
        return render(request,'result.html',{'notfound':notfound,
                                             "identities":identities,
                                             "departments":departments})


def allResults(request):
    teachers = Teacher.objects.all()
    return render(request,'result.html',{"teachers":teachers,
                                         "identities":identities,
                                         "departments":departments})




from django.db import models

教授 = "教授"
副教授 = "副教授"
讲师 = "讲师"
class Identity(models.Model):
    identity = models.CharField(max_length=20,choices=
                    [(教授, '教授'), 
                     (副教授, '副教授'),
                     (讲师,'讲师')])
    
艺术教研中心= "艺术教研中心"
传播学系= "传播学系"
数字媒体系= "数字媒体系"
设计系= "设计系"
class Department(models.Model):
    department = models.CharField(max_length=20,choices=
                    [(艺术教研中心, '艺术教研中心'), 
                     (传播学系, '传播学系'),
                     (数字媒体系,'数字媒体系'),
                     (设计系,'设计系')])

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    @classmethod
    def create_teacher(cls,name,identity,department):
        identity_obj,_ = Identity.objects.get_or_create(identity)
        department_obj,_ = Department.objects.get_or_create(department)
        teacher = cls.objects.create(name = name,
                                     identity = identity_obj,
                                     department = department_obj)
        return teacher
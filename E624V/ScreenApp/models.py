from django.db import models

# Create your models here.
class Identity(models.TextChoices):
    教授 = '教授',"教授"
    副教授 = '副教授',"副教授"
    讲师 = '讲师',"讲师"
    
class Department(models.TextChoices):
    艺术教研中心= '艺术教研中心',"艺术教研中心"
    传播学系= '传播学系',"传播学系"
    数字媒体系= '数字媒体系',"数字媒体系"
    设计系= '设计系',"设计系"

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20,
                                choices=Identity.choices,
                                default=Identity.教授)
    department = models.CharField(max_length=20,
                                  choices=Department.choices,
                                  default=Department.数字媒体系)
    def __str__(self) -> str:
        return "%s,%s,%s\n" %(
            self.name,
            self.identity,
            self.department
        )
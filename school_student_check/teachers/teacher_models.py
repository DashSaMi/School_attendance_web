from django.db import models
from students.student_models import Studentinfo

class Teacherinfo(models.Model):
    teacher_name=models.CharField(max_length=50 , verbose_name="نام معلم")
    teacher_last_name=models.CharField(max_length=70,verbose_name="نام خانوادگی معلم")
    teacher_phone_number=models.IntegerField(verbose_name="شماره تلفن")
    student=models.ForeignKey(Studentinfo,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_last_name}"


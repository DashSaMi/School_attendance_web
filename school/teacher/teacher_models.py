from django.db import models

class Teacherinfo(models.Model):
    teacher_id = models.CharField(max_length=6, primary_key=True, unique=True, verbose_name="کد شش رقم معلم")
    teacher_name = models.CharField(max_length=50, verbose_name="نام معلم")
    teacher_last_name = models.CharField(max_length=70, verbose_name="نام خانوادگی معلم")
    teacher_phone_number = models.IntegerField(verbose_name="شماره تلفن")
    student = models.ForeignKey('student.Studentinfo', on_delete=models.CASCADE)
    teacher_field = models.ForeignKey('general_proccess.Field', on_delete=models.CASCADE, null=True)
    teacher_grade = models.ForeignKey('general_proccess.Grade', on_delete=models.CASCADE, null=True)
  

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_last_name}"
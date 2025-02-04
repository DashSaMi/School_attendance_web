from django.db import models

class Studentinfo(models.Model):
    frist_name = models.CharField(max_length=50, verbose_name="نام دانش اموز")
    last_name = models.CharField(max_length=70, verbose_name="نام خانوادگی دانش اموز")
    student_field = models.ForeignKey('general_proccess.Field', on_delete=models.CASCADE)
    student_grade = models.ForeignKey('general_proccess.Grade', on_delete=models.CASCADE)
    phone_number = models.IntegerField(verbose_name="شماره تلفن")

    def __str__(self):
        return f"{self.frist_name} {self.last_name}"
from django.db import models

class Studentinfo(models.Model):
    frist_name=models.CharField(max_length=50 , verbose_name="نام دانش اموز")
    last_name=models.CharField(max_length=70,verbose_name="نام خانوادگی دانش اموز")
    phone_number=models.IntegerField( verbose_name="شماره تلفن")

    def __str__(self):
        return f"{self.frist_name} {self.last_name}"

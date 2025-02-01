from django.db import models
from teachers.teacher_models import Teacherinfo
from students.student_models import Studentinfo

class Attendance(models.Model):
    teacher = models.ForeignKey(Teacherinfo, on_delete=models.CASCADE, related_name='attendances', verbose_name="نام معلم")
    student = models.ForeignKey(Studentinfo, on_delete=models.CASCADE, related_name='attendances', verbose_name="نام دانش اموز")
    date = models.DateField(verbose_name="تقویم")  
    is_present = models.BooleanField(default=False, verbose_name="حاضر یا غایب") 
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="روز کلاس")

    def __str__(self):
        return f"{self.student.frist_name} {self.student.last_name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
from django.shortcuts import render
from .teacher_models import Teacherinfo

def Teacher_Table(request):
    all_info=Teacherinfo.objects.all()
    return render(request,"teacher/teacher.html",{"content":all_info})

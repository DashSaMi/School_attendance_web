from .teacher_models import Teacherinfo 
from django.shortcuts import render  

def teacher_page(request):  
    all_student=Teacherinfo.objects.all()
    return render(request, "teachers/t.html",{"content":all_student})  
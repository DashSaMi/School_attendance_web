from django.urls import path
from teacher.teacher_views import Teacher_Table

urlpatterns = [
    path('',Teacher_Table)
]
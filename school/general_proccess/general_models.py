from django.db import models  

class Field(models.Model):  
    field_name = models.CharField(max_length=70, verbose_name="نام رشته")  

    def __str__(self):  
        return f"{self.field_name}"  


class Grade(models.Model):  
    grade = models.CharField(max_length=50, verbose_name="پایه تحصیلی")  

    def __str__(self):  
        return f"{self.grade}"  


class Book(models.Model):  
    book_name = models.CharField(max_length=70, verbose_name="نام کتاب")  

    book_field = models.ForeignKey('general_proccess.Field', on_delete=models.CASCADE)  
    book_grade = models.ForeignKey('general_proccess.Grade', on_delete=models.CASCADE)  

    def __str__(self):  
        return f"{self.book_name} برای رشته {self.book_field} پایه {self.book_grade}"
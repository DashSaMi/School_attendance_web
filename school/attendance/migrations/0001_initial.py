# Generated by Django 5.1.5 on 2025-02-03 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تقویم')),
                ('is_present', models.BooleanField(default=False, verbose_name='حاضر یا غایب')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='روز کلاس')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='student.studentinfo', verbose_name='نام دانش اموز')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='teacher.teacherinfo', verbose_name='نام معلم')),
            ],
        ),
    ]

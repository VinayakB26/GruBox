from django.contrib import admin
from .models import Student,SubjectMarks,SubjectName,Topper

@admin.register(Student,SubjectMarks,SubjectName,Topper)
class StudentAdmin(admin.ModelAdmin):
    pass

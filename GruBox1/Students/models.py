from django.db import models

class Student (models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Class=models.IntegerField(null=False)
    RollNo=models.IntegerField(null=False)
    Semester=models.IntegerField(null=False)
    

class SubjectMarks(models.Model):
    RollNo=models.IntegerField(null=False)
    Class=models.IntegerField(null=False)
    SubjectId=models.IntegerField(null=False)
    Marks=models.IntegerField(null=False)
    


class SubjectName(models.Model):
    SubjectId=models.IntegerField(null=False)
    SubjectName=models.CharField(max_length=50)
    
    
class Topper(models.Model):
    TopperName = models.CharField(max_length=61)
    RollNo = models.IntegerField(null=False)
    Class = models.IntegerField(null=False)
    TotalMarks = models.IntegerField(null=False)
    
    
    
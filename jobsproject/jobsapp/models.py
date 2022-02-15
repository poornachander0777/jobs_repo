from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    CompanyName=models.CharField(max_length=30)
    JobName=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Experience=models.CharField(max_length=30)
    Salary=models.IntegerField()
    ContactNumber=models.CharField(max_length=30)
    Email=models.EmailField()
    Address=models.TextField()
class Mumbaijobs(models.Model):
    CompanyName=models.CharField(max_length=30)
    JobName=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Experience=models.CharField(max_length=30)
    Salary=models.IntegerField()
    ContactNumber=models.CharField(max_length=30)
    Email=models.EmailField()
    Address=models.TextField()
class Husnabadjobs(models.Model):
    CompanyName=models.CharField(max_length=30)
    JobName=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Experience=models.CharField(max_length=30)
    Salary=models.IntegerField()
    ContactNumber=models.CharField(max_length=30)
    Email=models.EmailField()
    Address=models.TextField()
class Punejobs(models.Model):
    CompanyName=models.CharField(max_length=30)
    JobName=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Experience=models.CharField(max_length=30)
    Salary=models.IntegerField()
    ContactNumber=models.CharField(max_length=30)
    Email=models.EmailField()
    Address=models.TextField()

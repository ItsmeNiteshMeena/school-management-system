from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    # detail=models.CharField(max_length = 50)
    phone=models.IntegerField()
    # subscribe=models.CharField(max_length = 50)
    gender=models.CharField(max_length = 50)
    dob=models.DateField()
    standard=models.CharField(max_length=50)
    profile_pic=models.FileField(upload_to = 'image/')
    address=models.CharField(max_length=50)
    # resume=models.FileField(upload_to = 'file/')
    password=models.CharField(max_length = 50)
    def __str__(self):
        return self.name 
    

class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)

class scheduled(models.Model):
    Subject=models.CharField(max_length=20)
    Day=models.CharField(max_length=10)
    Time=models.IntegerField()
    Teacher=models.CharField(max_length=20)    

    
class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.TextField()    
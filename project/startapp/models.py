from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.IntegerField()
    

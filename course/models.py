
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from challenges.models import challenge
class course (models.Model):
    courseid =models.CharField(max_length =20,primary_key=True )
    courseName = models.CharField(max_length =20)

class courseinstructure(models.Model):
    courseid= models.ManyToManyField(course)
    instructorname = models.ForeignKey(User, on_delete=models.CASCADE)

class studentincourse (models.Model):
    courseid =models.ForeignKey(course, on_delete=models.CASCADE)
    studentName = models.ManyToManyField(User)
    
class hwincourse (models.Model):
    hwname =models.CharField(max_length =20,primary_key=True )
    descreption =models.TextField ( )
    courseid =models.ForeignKey(course, on_delete=models.CASCADE )
    instructor = models.ManyToManyField(User)
    question = models.ManyToManyField(challenge)
    startDate =models.DateField(blank=True, null=True )
    endDate =models.DateField(blank=True, null=True)
    
    
    
    
'''
class courserelation (models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE, #primary_key=True 
    )
    courseid =models.ForeignKey(course,
        on_delete=models.CASCADE, #primary_key=True 
    ) 
'''
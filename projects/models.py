from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class project(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE, #primary_key=True 
    )
    name =  models.CharField(max_length =20 ,blank=False, null=False,unique=True,primary_key=True)
    language = models.CharField(max_length =20 ,blank=False, null=False)
    library =models.CharField(max_length =20 ,blank=True, null=True)
   

class File(models.Model):
   project = models.ForeignKey(project,
        on_delete=models.CASCADE, #primary_key=True 
   )
   filename =models.CharField(max_length=20)
   File = models.FileField()
# Create your models here.
#read_only_fields=['user']
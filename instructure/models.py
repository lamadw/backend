 
# Create your models here.
from django.db import models
class requestinstuctor (models.Model):
    username =models.CharField(max_length =20,primary_key=True )
    password1 = models.CharField(max_length =20)
    password2= models.CharField(max_length =20)
    email = models.EmailField()

class provedinstuctor (models.Model):
    requestinstuctor = models.ForeignKey(requestinstuctor,to_field="username",on_delete=models.CASCADE)
    proved = models.BooleanField(default=False,blank=False,null=False)

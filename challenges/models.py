
from django.db import models
from django.contrib.auth.models import User

def upload_input_challenge(instance,filename):
   return "challenges/{challenge}/{filename}".format(challenge=instance.challenge,filename=filename)
class challenge (models.Model):
   challengeName =models.CharField(max_length=20,unique=True ,primary_key=True)
   description =models.TextField()
 
class texttestcase(models.Model): 
   challenge = models.ForeignKey(challenge,to_field='challengeName', on_delete=models.CASCADE)
   Input = models.TextField()
   output = models.TextField()

class imagetestcase(models.Model): 
   challenge = models.ForeignKey(challenge,to_field='challengeName', on_delete=models.CASCADE)
   Input = models.ImageField(upload_to=upload_input_challenge,blank=False, null=False )
   output = models.ImageField()
    

from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import settings
class userrule(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True, )
    role = models.CharField(max_length =20,)
from django.contrib import admin
from .models import challenge,texttestcase,imagetestcase
admin.site.register(texttestcase)
admin.site.register(imagetestcase)
admin.site.register(challenge)
# Register your models here.

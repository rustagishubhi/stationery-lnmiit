from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminOfficeProfileInfo(models.Model):

   user = models.OneToOneField(User,related_name='adminuser',on_delete=models.CASCADE)
   def __str__(self):
       return self.user.username

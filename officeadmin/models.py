from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

   user = models.OneToOneField(User,related_name='adminuser',on_delete=models.CASCADE)

   fId = models.CharField(max_length=100)
   def __str__(self):
       return self.user.username

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FacultyProfileInfo(models.Model):
    fid = models.CharField(max_length=100,primary_key=True)
    user = models.OneToOneField(User,related_name='faculty',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

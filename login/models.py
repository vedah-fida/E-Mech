from django.db import models
from services.models import Services


# Create your models here.

# admin users table
class Users(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25)




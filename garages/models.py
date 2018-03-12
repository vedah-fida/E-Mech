from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class RegisterGarage(models.Model):
    garage_name = models.CharField(max_length=45)
    garage_location = models.CharField(max_length=50)

    #the garage admin will be the mechanic who registered it
    #associate this field to the models.User field
    """
    garage_admin = models.
    """
    garage_email = models.EmailField()
    garage_telephone = models.IntegerField()

    def __str__(self):
        return self.garage_name

    def get_absolute_url(self):
        return reverse("garages:register_garage")


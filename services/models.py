from django.db import models


# Create your models here.
# services table

class Services(models.Model):
    service_name = models.CharField(max_length=30)

    def __str__(self):
        return self.service_name

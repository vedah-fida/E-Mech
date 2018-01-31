from django.db import models
from services.models import Services

# Create your models here.
# mechanics table
class Mechanics(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    service_name = models.ForeignKey(Services,
                                     on_delete=models.CASCADE)  # The services model has been imported from the
    # app Services models

    def __str__(self):
        return self.username
from django.db import models

# Create your models here.

class CertificationModel(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400)
    image = models.CharField(max_length = 600)
    section = models.CharField(max_length = 40)
    link = models.CharField(max_length = 400)

    def __str__(self):
        return self.name
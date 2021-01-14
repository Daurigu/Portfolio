from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StartModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name='startModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

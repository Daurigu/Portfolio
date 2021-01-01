from django.db import models

# Create your models here.

class StartModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey('auth.user', related_name='startModel', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
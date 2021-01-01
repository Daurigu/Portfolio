from django.db import models

# Create your models here.
class TechSectionModel(models.Model):
    section = models.CharField(max_length = 40)
    description = models.CharField(max_length = 500)
    owner = models.ForeignKey('auth.user', related_name='TechModel', on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.section

class TechModel(models.Model):
    section = models.ForeignKey(TechSectionModel, on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400)
    image = models.CharField(max_length = 600)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Rat(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length= 30)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
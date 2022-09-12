from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Fecha(models.Model):
    birthday = models.DateField()

from django.db import models

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=60,)
    email = models.CharField(max_length=60,)
    numero = models.CharField(max_length=60,)
    code = models.CharField(max_length=60,)
    adresse = models.CharField(max_length=60,)
    desc = models.TextField()
    timestamp = models.DateTimeField()


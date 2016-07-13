from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import uuid
import random

class Associados(models.Model):

    def randomzin():
      x = random.randint(1, 200000)
      return x

    id = models.CharField(max_length=6,primary_key=True, default=randomzin, editable=True)
    Nome = models.CharField(max_length=200, unique = True)
    RG = models.CharField(max_length=12)
    CPF = models.CharField(max_length=12)
    RA = models.CharField(max_length=20, null=True, blank=True)
    Data_de_Associacao = models.DateField(
            default=timezone.now)



    def publish(self):
        self.save()

    def __str__(self):
        return self.Nome

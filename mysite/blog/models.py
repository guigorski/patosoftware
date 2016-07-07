from django.db import models

from django.db import models
from django.utils import timezone

class Post(models.Model):

    Nome = models.CharField(max_length=200)
    RG = models.CharField(max_length=200)
    CPF = models.CharField(max_length=200)
    created_date = models.DateField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

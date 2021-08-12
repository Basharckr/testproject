from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    game = models.CharField(max_length=200, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)





from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    chip_id = models.CharField(max_length=50)

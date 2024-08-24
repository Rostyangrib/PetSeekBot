from django.db import models

class Pet(models.Model):
    name = models.CharField('Имя питомца', max_length = 50)
    breed = models.CharField('Порода', max_length = 50)
    age = models.IntegerField()
    idshka = models.CharField('Идентификатор', max_length = 50)

    def __str__(self):
        return self.name
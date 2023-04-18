from django.db import models

# Create your models here.

class Phone(models.Model):

    name = models.CharField('Phone name', max_length=60)
    price = models.PositiveIntegerField('Phone price')

    def __str__(self):
        return self.name
    
class Notebook(models.Model):

    name = models.CharField('Notebook name', max_length=60)
    price = models.PositiveIntegerField('Notebook price')

    def __str__(self):
        return self.name
    
from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    desccription = models.CharField(max_length=200)
    def __str__(self):
        return self.name+' '+self.desccription
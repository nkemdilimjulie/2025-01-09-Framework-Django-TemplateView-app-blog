from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)  # CharField with a max length of 100

    def __str__(self):
        return self.name[:50]

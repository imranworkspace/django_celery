from django.db import models

# Create your models here.
from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField()

    def __str__(self):
        return self.title
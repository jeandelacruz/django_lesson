from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name

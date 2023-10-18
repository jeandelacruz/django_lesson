from django.db import models


# Create your models here.
class Author(models.Model):  # authors_author
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name

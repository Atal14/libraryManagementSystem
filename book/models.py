from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    isbn = models.CharField(unique=True)
    publication_date = models.DateTimeField()
    genre = models.CharField(blank=True)
    available_copies = models.IntegerField(default=0)

    class Meta():
        db_table = 'book'

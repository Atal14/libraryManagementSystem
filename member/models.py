from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    member_id = models.IntegerField()
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField()


    class Meta():
        db_table = 'member'
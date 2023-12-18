from django.db import models

# Create your models here.
class Record(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
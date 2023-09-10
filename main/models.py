from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=255)
    npm = models.IntegerField(default=0)
    kelas = models.TextField()
    item_name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    rating = models.CharField(max_length=3)
    reviews = models.TextField(default=0)

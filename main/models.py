from django.db import models

class main(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    rating = models.CharField(max_length=3)
    reviews = models.TextField(default=0)

from django.db import models
from django.contrib.auth.models import User


class Main(models.Model):
    npm = models.IntegerField(default=0)
    kelas = models.TextField()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    image = models.URLField(max_length=1000, default="insert image url here")
    amount = models.IntegerField(default=0)
    description = models.TextField(default="describe the product")
    rating = models.CharField(max_length=3, default=0)
    reviews = models.TextField(default="type your review here")

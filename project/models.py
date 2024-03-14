from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()
    picture = models.ImageField(upload_to='images/')
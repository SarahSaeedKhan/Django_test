from django.db import models


# Create your models here.
class Products(models.Model):
    slug = models.SlugField(unique=True)  # unique id
    name = models.CharField(max_length=255)
    price = models.IntegerField()

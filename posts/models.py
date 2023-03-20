from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=155, db_index=True)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    rate = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
from _decimal import Decimal

from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=155, db_index=True)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    rate = models.FloatField(default=0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
class Review(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} -> {self.post.title}'
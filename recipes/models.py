from django.db import models
from foodieApp.models import Category

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    
    def __str__(self):
        return self.name
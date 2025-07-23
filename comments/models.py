from django.db import models
from recipes.models import Recipe

# Create your models here.

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]  # Return the first 50 characters of the comment text
    
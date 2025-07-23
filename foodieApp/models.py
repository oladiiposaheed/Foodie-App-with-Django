from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    #description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

    
    
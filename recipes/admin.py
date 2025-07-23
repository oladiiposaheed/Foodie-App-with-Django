from django.contrib import admin
from recipes.models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date')
    search_fields = ('name', 'category__name') # Enables searching by category name, category__name means we can search by the related field's name
    
admin.site.register(Recipe, RecipeAdmin)  # Registering Recipe model without custom admin class


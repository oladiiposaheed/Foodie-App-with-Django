from django.contrib import admin
from foodieApp.models import Category, Recipe
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)
    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date')
    search_fields = ('name', 'category__name') # Enables searching by category name, category__name means we can search by the related field's name
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)  # Registering Recipe model without custom admin class


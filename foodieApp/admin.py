from django.contrib import admin
from foodieApp.models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)
    

admin.site.register(Category, CategoryAdmin)

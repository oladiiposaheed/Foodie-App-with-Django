from django.contrib import admin
from comments.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'text', 'date')
    search_fields = ('content',)  # Enables searching by author's username
    
admin.site.register(Comment, CommentAdmin)  # Registering Comment model with custom admin class
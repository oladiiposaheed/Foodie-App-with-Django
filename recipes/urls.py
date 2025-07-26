from django.urls import path
from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>', views.recipe_details, name='recipe_details'),
]

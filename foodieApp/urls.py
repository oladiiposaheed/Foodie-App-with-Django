from django.urls import path
from foodieApp import views

app_name = 'foodieApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:category_id>/', views.category_recipes, name='category_recipes'),
]

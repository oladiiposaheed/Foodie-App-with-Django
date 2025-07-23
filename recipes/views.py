from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe

# Create your views here.
def recipes(request):
    recipes_list = Recipe.objects.all()
    dict = {'recipes': recipes_list}
    print(dict)
    return HttpResponse("This is the recipes page.")
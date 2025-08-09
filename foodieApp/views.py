from django.shortcuts import render
from foodieApp.models import Category
from recipes.models import Recipe
from django.http import HttpResponse
# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories,}
    return render(request, 'foodieApp/index.html', context)


def category_recipes(request, category_id):
    try:
        category_recipes = Recipe.objects.filter(category=category_id)
        category = Category.objects.get(pk=category_id)
        dict = {'category_recipes': category_recipes, 'category': category}
        return render(request, 'foodieApp/category_recipes.html', dict)
    except Category.DoesNotExist:
        return HttpResponse('Category not found', status=404)
        
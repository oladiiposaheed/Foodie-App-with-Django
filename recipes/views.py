from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe
from django.db.models import Count, Avg, Sum, Max, Min, Q

# Create your views here.
def recipes(request):
    #recipes_list = Recipe.objects.all()
    #recipes_list = Recipe.objects.filter(category__name__icontains='West African Cuisine')
    #recipes_list = Recipe.objects.exclude(category__name__icontains='West African Cuisine')
    #recipes_list = Recipe.objects.exclude(category__name__exact='Pizza')
    #recipes_list = Recipe.objects.exclude(name__contains='Pizza')
    #recipes_list = Recipe.objects.filter(category__name__exact='West African Cuisine').exclude(category__name__icontains='Pizza').order_by('-date')
    #recipes_list = Recipe.objects.all()[:2]  # Fetching the first 2 recipes
    #recipes_list = Recipe.objects.aggregate(total_recipes_id=Count('id'))
    #recipes_list = Recipe.objects.aggregate(average_id=Avg('id')) 
    #recipes_list = Recipe.objects.aggregate(total_id=Sum('id'))
    #recipes_list = Recipe.objects.aggregate(total_id=Sum('id')**2) # Squaring the sum of IDs
    #recipes_list = Recipe.objects.aggregate(max_id=Max('id'))
    #recipes_list = Recipe.objects.aggregate(min_id=Min('id'))
    #recipes_list = Recipe.objects.filter(id__gte=recipes_list['min_id'])
    #recipes_list = Recipe.objects.filter(id__gt=3)
    #recipes_list = Recipe.objects.filter(Q(name__contains='Pizza') | Q(description__contains='fluffy')).order_by('-date')
    #recipes_list = Recipe.objects.filter(id__gt=2).values()
    #recipes_list = Recipe.objects.filter(id__gt=2).values('name', 'description', 'date')
    #recipes_list = Recipe.objects.filter(id__gt=2).values_list()
    recipes_list = Recipe.objects.filter(id__gt=2).values_list('name', 'description', 'date')
    #recipes_list = Recipe.objects.filter(id__gt=3).count()
    recipes_list = Recipe.objects.filter(id__gt=3).exists()
    recipes_list = Recipe.objects.filter(id__gt=10).exists()
    recipes_list = Recipe.objects.filter(name__contains='Pizza').exists()
    dict = {
        'recipes_list': recipes_list,
    }
    print(dict)
    return HttpResponse("This is the recipes page.")
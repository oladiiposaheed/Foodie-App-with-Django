from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
   

def index(request):
    food_data = ['Rice', 'Beans', 'Chicken', 'Fish', 'Eggs', 'Pasta', 'Bread', 'Vegetables']
    
    dict = {'food': food_data}
    return render(request, 'sandbox/index.html', context=dict)
    


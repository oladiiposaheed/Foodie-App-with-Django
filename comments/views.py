from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def comments(request):
    return HttpResponse("This is the comments page.")
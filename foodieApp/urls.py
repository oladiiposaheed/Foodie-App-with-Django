from django.urls import path
from foodieApp import views

app_name = 'foodieApp'
urlpatterns = [
    path('', views.index, name='index'),
]

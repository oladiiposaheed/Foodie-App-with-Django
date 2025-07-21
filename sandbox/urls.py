from django.urls import path
from sandbox import views

#app_name = 'sandbox'
urlpatterns = [
    # Add your URL patterns here
    path('index', views.index),
]
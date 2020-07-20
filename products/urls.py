from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index),
    path('uploads/', views.uploads, name="uploads")


]

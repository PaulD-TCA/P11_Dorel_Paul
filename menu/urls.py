from django.urls import path

from . import views

urlpatterns = [
    path('menu_generation/', views.menu_generation, name='menu_generation'),
    ]

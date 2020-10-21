from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results_page/', views.results, name='results_page'),
    path('food_page/<int:id>/', views.food_page, name='food_page'),
    path('save_page/<int:id>/', views.save_page, name='save_page'),
    path('my_favourites_page/', views.my_favourites, name='my_favourites_page'),
]

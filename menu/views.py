from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from menu import menu_builder
from search_and_sub.models import Product

# Create your views here.
def menu_generation(request):
    """Display the legal notice."""
    template = loader.get_template('menu/menu_gene.html')
    m_b = menu_builder.MenuBuild()
    starter = Product.objects.filter(id=m_b.random_starter()[0])
    main_dish = Product.objects.filter(id=m_b.random_main_dish()[0])
    dessert = Product.objects.filter(id=m_b.random_dessert()[0])

    context = {
    'starter':starter,
    'main_dish':main_dish,
    'dessert':dessert,
                }
    return HttpResponse(template.render(context, request))

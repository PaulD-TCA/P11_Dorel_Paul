import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Backup
from django.contrib.auth.models import User
from .forms import NameForm
# import os

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    """Display the main web page."""
    #template = loader.get_template('search_and_sub/home.html')
    context = {}
    # if os.environ.get('ENV') == 'PRODUCTION':
    #     print("production")
    # else:
    #     print(" pas production")
    return HttpResponse(template.render(context, request))

def food_page(request, id):
    """Display the food page with a summary."""
    template = loader.get_template('search_and_sub/food_page.html')
    food_details = Product.objects.filter(id=id)
    context = {'food_details':food_details,}
    return HttpResponse(template.render(context, request))

def save_page(request, id):
    """Allow the user to save a ssearched food."""
    template = loader.get_template('search_and_sub/save_page.html')
    food_details = Product.objects.filter(id=id)
    current_user = request.user.id
    food_to_save = Backup(p_id_id=id, u_id_id=current_user)
    food_to_save.save()
    context = {'food_details':food_details,}
    return HttpResponse(template.render(context, request))

def results(request):
    """Display the results of a query."""
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            search_string = form.cleaned_data['your_name']
            words = list(search_string.split(" "))
            for word in words:
                foods = Product.objects.filter(p_name__icontains=search_string)[:9]
            template = loader.get_template('search_and_sub/results_page.html')
            context = {
            'foods':foods,
            }
            return HttpResponse(template.render(context, request))
    template = loader.get_template('search_and_sub/results_page.html')
    context = {}
    logger.info('New search', exc_info=True, extra={
    'request': request,
    })
    return HttpResponse(template.render(context, request))

def my_favourites(request):
    """Display user saved foods."""
    current_user = request.user.id
    favourites_list = Product.objects.filter(backup__u_id_id=current_user)
    template = loader.get_template('search_and_sub/my_favourites_page.html')
    context = {'favourites_list':favourites_list}
    return HttpResponse(template.render(context, request))

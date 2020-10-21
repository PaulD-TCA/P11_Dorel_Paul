from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def legal_notice(request):
    """Display the legal notice."""
    template = loader.get_template('basics_screens/legal_notice_page.html')
    context = {}
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def reserve_mainpage(request):
    template = loader.get_template("reserve_mainpage.html")
    context = {}
    return HttpResponse(template.render(context, request))



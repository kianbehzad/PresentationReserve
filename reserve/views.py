from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reserve_mainpage(request):
    return HttpResponse("reserved")



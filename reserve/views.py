from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myadmin.models import Datetime


# Create your views here.

def reserve_mainpage(request):
    stdnum = request.GET.get("name")
    name = request.GET.get("name1")
    email = request.GET.get("email")
    date = request.GET.get("service")
    topic = request.GET.get("message")
    if stdnum == None:#reserve_mainpage
        template = loader.get_template("reserve_mainpage.html")
        all_Datetime = Datetime.objects.all()
        context = {'all_Datetime': all_Datetime}
        return HttpResponse(template.render(context, request))
    #else #verification_page
    template = loader.get_template("reserve_verification.html")
    context = {}
    return HttpResponse(template.render(context, request))




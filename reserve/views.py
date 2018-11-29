from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myadmin.models import Datetime
from .models import Student
import random
from django.core.mail import send_mail


# Create your views here.

def reserve_mainpage(request):
    stdnum = request.GET.get("name")
    name = request.GET.get("name1")
    email = request.GET.get("email")
    date_pk = request.GET.get("service")
    topic = request.GET.get("message")
    if stdnum == None:#reserve_mainpage
        template = loader.get_template("reserve_mainpage.html")
        all_Datetime = Datetime.objects.all()
        context = {'all_Datetime': all_Datetime}
        return HttpResponse(template.render(context, request))

    #else #verification_page
    for _student in Student.objects.all():
        if _student.email == email:
            _student.delete()
    datetime = None
    for _datetime in Datetime.objects.all():
        if _datetime.pk == int(date_pk):
            datetime = _datetime
    verification_code = random.randint(10000, 99999)
    student = Student(stdnum=stdnum, name=name, email=email, datetime=datetime, topic=topic, is_verified=False,
                      verification_code=verification_code)
    verification_link_str = request.get_host()+'/reserve/verificationlink/?email='+email+'&verificationcode='+str(verification_code)
    send_mail(
        'Reservation Verification Link',
        'your Reservation verification link is: <a href="'+verification_link_str+'">Click</a>',
        'community@class.ir',
        [student.email],
        fail_silently=True,
    )
    student.save()
    template = loader.get_template("reserve_verification.html")
    context = {}
    return HttpResponse(template.render(context, request))

def verification_link(request):
    email = request.GET.get("email")
    verificationcode = request.GET.get("verificationcode")
    result = 'FAILED'
    for _student in Student.objects.all():
        if email == _student.email and _student.verification_code == verificationcode:
            _student.is_verified = True
            _student.save()
            result = 'SUCCESSFUL'

    template = loader.get_template("reserve_is_verified.html")
    context = {'result': result}
    return HttpResponse(template.render(context, request))


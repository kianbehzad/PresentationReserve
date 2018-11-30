from django.shortcuts import render
from .models import Datetime
from reserve.models import Student
from django.http import HttpResponse
from PresentationReserve.settings import BASE_DIR
import os

# Create your views here.

def list(request):
    filepath = os.path.join(BASE_DIR, "media") + '/list.xlsx'
    print(filepath)
    with open(filepath, 'rb') as fp:
        data = fp.read()
    filename = 'reservation_list.xlsx'
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename  # force browser to download file
    response.write(data)
    return response
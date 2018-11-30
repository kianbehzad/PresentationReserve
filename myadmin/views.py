from django.shortcuts import render
from .models import Datetime
from reserve.models import Student
from django.http import HttpResponse
from PresentationReserve.settings import BASE_DIR
import os
import openpyxl

# Create your views here.

def list(request):
    # create the list
    book = openpyxl.Workbook()
    sheet = book.active
    cnt = 1
    for st in Student.objects.all():
        if st.is_verified:
            sheet['A' + str(cnt)] = st.email
            sheet['B' + str(cnt)] = st.topic
            sheet['C' + str(cnt)] = st.datetime.__str__()
            cnt += 1
    os.chdir(os.path.join(BASE_DIR, "media"))
    if os.path.exists('list.xlsx'):
        os.remove('list.xlsx')
    book.save('list.xlsx')

    filepath = os.path.join(BASE_DIR, "media") + '/list.xlsx'
    print(filepath)
    with open(filepath, 'rb') as fp:
        data = fp.read()
    filename = 'reservation_list.xlsx'
    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename  # force browser to download file
    response.write(data)
    return response
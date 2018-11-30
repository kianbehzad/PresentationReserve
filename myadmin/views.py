from django.shortcuts import render
from .models import Datetime
from reserve.models import Student
from django.http import HttpResponse
from PresentationReserve.settings import BASE_DIR
import os
import openpyxl

# Create your views here.

def sort_datatime(elem):
    return elem.datetime.year*365 + elem.datetime.month*30 + elem.datetime.day

def list(request):
    # create the list
    student_list = []
    for st in Student.objects.all():
        if st.is_verified:
            student_list.append(st)
    student_list.sort(key=sort_datatime)
    book = openpyxl.Workbook()
    sheet = book.active
    cnt = 2
    sheet['A1'] = 'EMAIL'
    sheet['B1'] = 'STUDENT NUMBER'
    sheet['C1'] = 'NAME'
    sheet['D1'] = 'TOPIC'
    sheet['E1'] = 'DATE TIME'
    for st in student_list:
        sheet['A' + str(cnt)] = st.email
        sheet['B' + str(cnt)] = st.stdnum
        sheet['C' + str(cnt)] = st.name
        sheet['D' + str(cnt)] = st.topic
        sheet['E' + str(cnt)] = st.datetime.__str__()
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
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
    sheet['A1'] = 'NUM'
    sheet['B1'] = 'EMAIL'
    sheet['C1'] = 'STUDENT NUMBER'
    sheet['D1'] = 'NAME'
    sheet['E1'] = 'TOPIC'
    sheet['F1'] = 'DATE TIME'
    num = 1
    for i in range(len(student_list)):
        if i >= 1 and student_list[i].datetime != student_list[i-1].datetime:
            num = 1
        sheet['A' + str(cnt)] = num
        sheet['B' + str(cnt)] = student_list[i].email
        sheet['C' + str(cnt)] = student_list[i].stdnum
        sheet['D' + str(cnt)] = student_list[i].name
        sheet['E' + str(cnt)] = student_list[i].topic
        sheet['F' + str(cnt)] = student_list[i].datetime.__str__()
        num += 1
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
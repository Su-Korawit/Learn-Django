from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

allTable = [
    {'id': 1, 'lastLecture': datetime(2024, 11, 1), 'grade': 42, 'codeSubject': 'ค32101', 'teacherName': 'ปิยวรรณ', 'codeRoom': '443', 'period': 1, 'day': 'Monday'},
    {'id': 2, 'lastLecture': datetime(2024, 11, 1), 'grade': 41,'codeSubject': 'ว31105', 'teacherName': 'ฉัตราภรณ์', 'codeRoom': '434', 'period': 2, 'day': 'Tuesday'},
    {'id': 3, 'lastLecture': datetime(2024, 10, 30), 'grade': 42,'codeSubject': 'ว31106', 'teacherName': 'ณรงณ์', 'codeRoom': '431', 'period': 3, 'day': 'Friday'},
]

def tablepage(request):
    context = {'table': allTable}
    return render(request, 'appTable/tablepage.html', context)

def changeTablePage(request, grade):
    searchTable = None
    try:
        searchTable = [s for s in allTable if s['grade'] == grade]
    except IndexError:
        print(e)
    context = {'table': searchTable}
    return render(request, 'appTable/changeTablePage.html', context)
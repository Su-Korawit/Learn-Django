from django.shortcuts import render
from django.http.response import HttpResponse


def tablepage(request):
    return render(request, 'appTable/tablepage.html')

def changeTablePage(request, grade):
    return render(request, 'appTable/changeTablePage.html', context={ 'grade':grade })
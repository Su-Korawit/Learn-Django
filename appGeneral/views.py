from django.shortcuts import render
from django.http.response import HttpResponse


def homepage(request):
    return render(request, 'appGeneral/homepage.html')

def aboutme(request):
    return render(request, 'appGeneral/aboutme.html')
# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse('Welcome to emobilis')
def About(request):
    return HttpResponse('About eMobilis')
def Services(request):
    return HttpResponse('Fullstack development')
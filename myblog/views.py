from django.shortcuts import render

# Create your views here.

# pawan ne likha hai yeh 

from django.http import HttpResponse

def home(request):
    return HttpResponse('hello')
    
def about(request):
    return HttpResponse('about')
    
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Go for a run!")

def february(request):
    return HttpResponse("Walk 5 km!")
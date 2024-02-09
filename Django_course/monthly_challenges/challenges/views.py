from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    if month == "january":
        return HttpResponse("Go for a run!")
    elif month == "february":
        return HttpResponse("Read 20 mins")
    elif month == "march":
        return HttpResponse("Study for school")
    else:
        return HttpResponseNotFound("No challenges were recorded for this month")

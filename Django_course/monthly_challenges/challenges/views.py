from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Challenges dictionary
monthly_challenges = {
    "january": "Go for a run",
    "february": "Read 20 mins",
    "march": "Study for school",
    "april": "Study some more!",
    "may": "Play some tennis",
    "june": "Go to the beach",
    "july": "Do some coding",
    "august": "Learn a new skill",
    "september": "Build a videogame",
    "october": "Get some good grades",
    "november": "Play some sports",
    "december": "Relax"
}

# Views Functions
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        capitalized_month = month.capitalize()
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>" 
    return HttpResponse(response_data)

def monthly_challenge_int(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Please enter a valid month</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Please enter a valid month!</h1>")

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
def monthly_challenge_int(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Please enter a valid month!")

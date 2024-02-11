from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_int(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        raise Http404()
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        for key, value in monthly_challenges.items():
            if value == challenge_text:
                challenge_key = key
                break
        else:
            challenge_key = None

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": challenge_key
        })
    except:
        raise Http404()

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def january(request):
#     return HttpResponse("This works!!!")
#
# def february(request):
#     return HttpResponse("Go for Run!!!")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for m in months:
        capitalized_month = m.capitalize()
        month_path = reverse("parag", args = [m])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



monthly_challenges = {
    "january" : "Goa Trip!!!",
    "february" : "Leh Ladakh Trip!!!",
    "march" : "Andaman & Nicobar Trip!!!",
    "april" : "Kerala Trip",
    "may" : "Rajasthan Trip",
    "june" : "Pondicherry Trip",
    "july" : "Delhi Trip",
    "august" : "Kashmir Trip",
    "september" : "Jammu trip",
    "october" : "Chandhigard Trip",
    "november" : "Sikkim Trip",
    "december" : "Daman & Diu Trip"

}

def monthly_challenge_by_number(request, m):
    months = list(monthly_challenges.keys())

    if 0 < m > len(months):
        return HttpResponseNotFound("Invalid Month")


    redirect_month = months[m - 1]
    redirect_path = reverse("parag", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)

def month(request, m):
    try:
        challenge_text = monthly_challenges[m]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")

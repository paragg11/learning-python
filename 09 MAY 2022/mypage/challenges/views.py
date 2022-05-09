from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def january(request):
#     return HttpResponse("This works!!!")
#
# def february(request):
#     return HttpResponse("Go for Run!!!")

monthly_challenges = {
    "january" : "This works!!!",
    "february" : "Go for Run!!!"


}

def monthly_challenge_by_number(request, m):
    return HttpResponse(m)

def month(request, m):
    try:
        challenge_text = monthly_challenges[m]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid month")

from django.http import HttpResponse
from datetime import date
from django.shortcuts import render

# Create your views here.
# def index.css(request):
#     return HttpResponse("Parag")

all_posts = [
    {
        "slug" : "Charts1",
        "image" : "d3.jpg",
        "author" : "Parag",
        "date" : date(2022,1,1),
        "title" : "Trends",
        "excerpt" : "There are upwards, downwards and sideways trends.1",
        "content" : "Trading Types - Long term, Swing, Intraday, Positional"
    },
    {
        "slug": "Charts2",
        "image": "d3.jpg",
        "author": "Parag",
        "date": date(2022, 1, 1),
        "title": "Trends",
        "excerpt": "There are upwards, downwards and sideways trends.2",
        "content": "Trading Types - Long term, Swing, Intraday, Positional"
    },
    {
        "slug" : "Charts3",
        "image" : "d3.jpg",
        "author" : "Parag",
        "date" : date(2022,1,1),
        "title" : "Trends",
        "excerpt" : "There are upwards, downwards and sideways trends.3",
        "content" : "Trading Types - Long term, Swing, Intraday, Positional"
    },
    {
        "slug": "Charts4",
        "image": "d3.jpg",
        "author": "Parag",
        "date": date(2022, 1, 1),
        "title": "Trends",
        "excerpt": "There are upwards, downwards and sideways trends.4",
        "content": "Trading Types - Long term, Swing, Intraday, Positional"
    }

]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[(-1*len(all_posts)):]
    #latest_posts =sorted_posts[:]
    return render(request, "nse/index.html",{
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "nse/all-posts.html")

def post_detail(request, slug):
    return render(request, "nse/post-detail.html")

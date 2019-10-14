from django.shortcuts import render,redirect

import datetime as dt
from .models import Picture
# Create your views here.
def welcome(request):
        return render(request,'welcome.html')


def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})
def picture(request):
    
        picture = Picture.objects.all()
def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("category")
        searched_pictures = Picture.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"picture": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message}) 
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from .models import Picture
# Create your views here.
def welcome(request):
        return render(request,'welcome.html')
def picture(request):
    gallery= Picture.get_all_pictures()
    return render (request,'all-gallery/picture.html',{"gallery":gallery})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})


def filter_by_location(request,location_id):
   
   pictures = Picture.filter_by_location(id=location_id )
   return render (request,"all-gallery/location.html", {"pictures":pictures})


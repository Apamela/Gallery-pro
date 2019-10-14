from django.shortcuts import render,redirect
from django.http import HttpResponse
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

def picture(request,picture_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/picture.html", {"picture":picture})
def filter_by_location(request,location_id):
   
   pictures = Picture.filter_by_location(id=location_id )
   return render (request,"all-gallery/location.html", {"pictures":pictures})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("category")
        searched_pictures = Picture.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"picture": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message}) 
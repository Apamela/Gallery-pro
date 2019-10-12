from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Picture
# Create your views here.

def gallery_of_day(request):
    date = dt.date.today()
    gallery = Picture.todays_gallery()
    return render(request,'all-gallery/today-gallery.html',{"date": date,})


def past_days_gallery(request,past_date):
    try:    
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)
    gallery = Picture.days_gallery(date)
    return render(request, 'all-gallery/past-gallery.html',{"date": date,"gallery":gallery})

    gallery = Picture.days_gallery(date)
    return render(request, 'all-gallery/past-gallery.html', {"date": date})
def gallery_today(request):
    date = dt.date.today()
    gallery = Picture.todays_gallery()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})
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
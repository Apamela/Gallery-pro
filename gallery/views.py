from django.shortcuts import render

# Create your views here.
def Welcome(request):
    return HttpResponse('Welcome to the Gallery')
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def favorites(request):
    return render(request, 'favorites.html')

def impressions(request):
    return render(request, 'impressions.html')

def mylink(request):
    return render(request, 'mylink.html')

def profile(request):
    return render(request, 'profile.html')

def secondarypage(request):
    return render(request, 'secondarypage.html')

def settings(request):
    return render(request, 'settings.html')

def visits(request):
    return render(request, 'visits.html')



from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def excavators(request):
    return render(request, 'excavators.html')

def prices(request):
    return render(request, 'prices.html')

def contact(request):
    return render(request, 'contact.html')
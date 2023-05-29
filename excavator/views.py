from django.shortcuts import render

def home(request):
    return render(request, 'excavator/home.html')

def about(request):
    return render(request, 'excavator/about.html')

def excavators(request):
    return render(request, 'excavator/excavators.html')

def prices(request):
    return render(request, 'excavator/prices.html')

def contact(request):
    return render(request, 'excavator/contact.html')
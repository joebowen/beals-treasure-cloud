from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "BealsTreasure/home.html")

def status(request):
    return render(request, "BealsTreasure/status.html")

def faq(request):
    return render(request, "BealsTreasure/faq.html")

def about(request):
    return render(request, "BealsTreasure/about.html")

def contact(request):
    return render(request, "BealsTreasure/contact.html")
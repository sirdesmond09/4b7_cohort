from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def contact_us(request):
    return render(request, "contact.html")
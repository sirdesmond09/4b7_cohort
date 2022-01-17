from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return HttpResponse("This is my about page and I am interested in it!!")
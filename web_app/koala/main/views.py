from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.


def home_page(request):
    return render(request, "home.html")


def contact_us(request):
    
    if request.method == "POST":
        request_data = dict(request.POST)
        request_data.pop('csrfmiddlewaretoken')
        data = {key:request_data.get(key)[0] for key in request_data}
        
        Contact.objects.create(**data)
        
    contacts = Contact.objects.all()
    
    data = {
        "contacts" : contacts
    }
    
    return render(request, "contact.html",data)
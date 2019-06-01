from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def home_view(request,*args, **kwargs):
    #This function loads the template with the given name and returns a Template object
    #template = loader.get_template('Home/home.html')
    return render(request,'Home/home.html',{})

def contact_view(request,*args, **kwargs):
    return render(request,'Contact/contact.html',{})
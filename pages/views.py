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

def login_view(request,*args,**kwargs):
    return render(request,'Login/login_page.html',{})

def start_page_view(request,*args, **kwargs):
    return render(request,'StartPage/start_page.html',{})

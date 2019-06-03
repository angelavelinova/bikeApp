from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm


# Create your views here.
def home_view(request,*args, **kwargs):
    #This function loads the template with the given name and returns a Template object
    #template = loader.get_template('Home/home.html')
    return render(request,'Home/home.html',{})

def contact_view(request,*args, **kwargs):
    return render(request,'Contact/contact.html',{})


def start_page_view(request,*args, **kwargs):
    return render(request,'StartPage/start_page.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signUp/signup.html', {'form': form})

def login_view(request):
     return render(request, 'Login/login_page.html', {})
    
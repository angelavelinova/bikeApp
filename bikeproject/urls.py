"""bikeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view,contact_view,login_view
from bike.views import bike_view_details, bike_creat_form

urlpatterns = [
    path('', home_view, name='home'),
	path('contact/', contact_view),
    path('admin/', admin.site.urls),
    path('bike_details/',bike_view_details),
    path('bike_form/',bike_creat_form),
    path('login_page/',login_view)
]

"""Pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#Users request pages by entering URLs into a browser and clicking links, so
#we’ll need to decide what URLs are needed. The home page URL is first:
#it’s the base URL people use to access the project.
from django.contrib import admin
from django.urls import path, include

#edit the default urls.py file in the pizzas folder
# the urlpatterns variable includes sets of URLs from 
# the apps in the project.
urlpatterns = [
    path('admin/', admin.site.urls), #includes the module admin.site.urls, which defines all the URLs that can be
                                    #requested from the admin site.
    path('', include('Pizzas.urls')),
    path('users/', include('users.urls')),   
]

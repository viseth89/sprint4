"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    
    
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^operation/$', views.operation, name='operation'),
    url(r'^odetails/$', views.odetails, name='odetails'),
    url(r'^alogin/$', views.alogin, name='alogin'),
    url(r'^alogin/$', views.alogin, name='alogin'),
    url(r'^help/$', views.help, name='help'),
    url(r'^create/$', views.create, name='create'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^ratings/$', views.ratings, name='ratings'),

]
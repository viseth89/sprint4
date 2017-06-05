from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h2>HEY!</h2>")

def viseth(request):
    return HttpResponse('<h2>viseth is learning this slowly, because views connects to urls, which connects to urls</h2>')

def vibol(request):
    return HttpResponse('<h2>vibol is also is also is learning this slowly, because views connects to urls, which connects to urls</h2>')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html ="Go to the " + '<a href="/rango/about/">About</a>' + "view"
    return HttpResponse(html)

def about(request):
    html ="Go to the " + '<a href="/rango/">Index</a>' + "view"
    return HttpResponse(html)
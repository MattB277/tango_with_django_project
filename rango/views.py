from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'yourname': 'Matthew Ballantyne',}
    return render(request, 'rango/about.html', context=context_dict)
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    html ="Go to the " + '<a href="/rango/">Index</a>' + " view"
    return HttpResponse(html)
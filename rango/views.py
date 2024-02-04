from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

# Create your views here.
def index(request):
    # query database for all categories stored
    # Order by likes desc.
    # Take top 5 /  all if < 5 records
    # Place list in context_dict to be passed to template
    cat_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = cat_list
    # first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'yourname': 'Matthew Ballantyne',}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # try to find cat with same slug as parameter
        category = Category.objects.get(slug = category_name_slug)
        # retrieve all of its associated pages
        pages = Page.objects.filter(category=category)

        # add results to context_dict
        context_dict['pages']=pages
        context_dict['category']=category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
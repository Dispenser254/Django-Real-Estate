from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices,  price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    active_realtors = Realtor.objects.all().filter(is_active=True)
    context = {
        'realtors': realtors,
        'active_realtors': active_realtors
    }
    return render(request, 'pages/about.html', context)

def terms(request):
    return render(request, 'pages/terms-conditions.html')
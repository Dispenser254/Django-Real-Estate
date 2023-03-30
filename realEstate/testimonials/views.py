from django.shortcuts import render
from .models import Testimonial

def index(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'pages/testimonials.html', {'testimonials': testimonials})

def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'pages/index.html', {'testimonials': testimonials})
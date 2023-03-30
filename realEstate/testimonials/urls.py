from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index, name='testimonials'),
    path('', views.home, name='testimonials'),
]
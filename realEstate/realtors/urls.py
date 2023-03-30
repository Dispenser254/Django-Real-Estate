from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='agents'),
    path('<int:realtor_id>', views.realtor, name='agent'),
]
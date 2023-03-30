from django.urls import path
from contacts.views import contact_us

urlpatterns = [
    path('contact-us/', contact_us, name='contact_us'),
]

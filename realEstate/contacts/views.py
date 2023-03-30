from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            subject = 'Contact Us Form Submission'
            message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [from_email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            return render(request, 'contacts/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_us.html', {'form': form})

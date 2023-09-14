from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
import os


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(f'The contact form subject from {name}', message,
                      email, [os.environ.get('EMAIL_TO')])

            return redirect('contact:success_contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': ContactForm(),
        'title': 'Contact Us'
    })


def success_contact(request):
    return render(request, 'contact/contact_success.html')

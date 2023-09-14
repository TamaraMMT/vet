from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        messages.success(
            request, 'Your message was sent. Thank you for contacting us!')
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail('The contact form subject ' + name, message,
                      email, ['dear0010011@gmail.com'])

            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': ContactForm(),
        'title': 'Contact Us'
    })

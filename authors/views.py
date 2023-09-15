from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('authors:success')
        else:
            messages.info(request, 'Sorry! form not sent. check all fields ')
    else:
        form = RegistrationForm()

    return render(request, 'authors/pages/register_view.html', {'form': form, 'form_action': reverse('authors:register')}, )


def success(request):
    return render(request, 'authors/pages/success_register.html')

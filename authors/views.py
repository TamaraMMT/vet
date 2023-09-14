from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors:success')
        else:
            messages.info(request, 'Sorry! form not sent. check all fields ')
    else:
        form = RegistrationForm()

    return render(request, 'authors/pages/register_view.html', {'form': form})


def success(request):
    return render(request, 'authors/pages/success_register.html')

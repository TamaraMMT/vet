from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, LoginForm


def register(request):
    if request.user.is_authenticated:
        return redirect('authors:login_success')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                if 'form_data' in request.session:
                    del request.session['form_data']
                messages.success(
                    request, 'Do you already have an account! Log in, please'
                )

                return redirect('authors:login')
            else:
                request.session['form_data'] = request.POST.dict()
                messages.info(
                    request, 'Sorry! Form not sent. Check all fields.')
        else:
            form_data = request.session.get('form_data', {})
            form = RegistrationForm(initial=form_data)

        return render(request, 'authors/pages/register_view.html', {
            'form': form,
            'form_action': reverse('authors:register'),
            'title': 'Register',
        })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('authors:login_success')
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username', '')
                password = form.cleaned_data.get('password', '')

                user_authenticate = authenticate(
                    username=username, password=password)

                if user_authenticate is not None:
                    login(request, user_authenticate)
                    messages.success(request, 'You are logged in')
                    return redirect('authors:login_success')
                else:
                    messages.error(request, 'Invalid credentials')
            else:
                messages.info(
                    request, 'Sorry! Form not sent. Check all fields.')

        return render(request, 'authors/pages/login.html', {
            'form': form,
            'form_action': reverse('authors:login'),
            'title': 'Login'
        })


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def login_success(request):
    return render(request, 'authors/pages/login_success.html', {
        'title': 'Login Successful'})

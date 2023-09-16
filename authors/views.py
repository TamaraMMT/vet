from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session['form_data'] = form.cleaned_data
            del request.session['form_data']
            messages.success(
                request, 'Do you already have an account! Log in, please')

            return redirect('authors:login')
        else:
            request.session['form_data'] = request.POST.dict()
            messages.info(request, 'Sorry! Form not sent. Check all fields.')
    else:
        form_data = request.session.get('form_data', {})
        form = RegistrationForm(initial=form_data)

    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register'),
        'title': 'Register',
    })


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:create'),
        'title': 'Login'}
    )


def login_create(request):
    return render(request, 'authors/pages/login.html', {'title': 'Login'})

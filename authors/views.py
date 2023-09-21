
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from authors.forms.post_form import AuthorPostForm
from blog.models import PostBlog, Category
from utils.pagination import make_pagination
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import RegistrationForm, LoginForm
from blog.models import PostBlog


def register(request):
    if request.user.is_authenticated:
        return redirect('authors:dashboard')
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
        return redirect('authors:dashboard')
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
                    return redirect('authors:dashboard')
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
    messages.info(request, 'You are logged out.')
    return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    posts = PostBlog.objects.filter(
        author=request.user
    )
    page_obj, pagination_range = make_pagination(request, posts, 6)

    return render(request, 'authors/pages/dashboard.html', {
        'title': 'Dashboard',
        'posts':  page_obj,
        'pagination_range': pagination_range,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def create_post(request):
    categories = Category.objects.all()
    form = AuthorPostForm(request.POST or None)

    if request.method == 'POST':
        form.instance.author = request.user
        if form.is_valid():
            post_blog = form.save()
            messages.success(request, 'This is your new post!')
            return redirect('blog:posts', pk=post_blog.pk)
        else:
            messages.error(request, 'The form is invalid.')

    return render(request, 'authors/pages/create_post.html', {
        'title': 'Create Post',
        'categories': categories,
        'form': form,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def edit_posts(request, pk):
    posts = get_object_or_404(PostBlog, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = AuthorPostForm(request.POST, instance=posts,
                              files=request.FILES or None)
        form.instance.author = request.user
        if form.is_valid():
            cover = request.FILES.get('cover', None)
            if cover:
                posts.cover = cover
            posts.save()
            messages.success(request, 'Your post was edited!')
            return redirect('blog:posts', pk=posts.pk)
    else:
        form = AuthorPostForm(instance=posts)

    return render(request, 'authors/pages/dashboard_edit_post.html', {
        'title': 'Edit Post',
        'form': form,
        'categories': categories,
        'posts': posts,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def delete_post(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    id = POST.get('id')

    posts = PostBlog.objects.filter(
        author=request.user,
        pk=id,
    ).first()
    if not posts:
        raise Http404()
    posts.delete()
    messages.success(request, 'Deleted')
    return redirect(reverse('authors:dashboard'))

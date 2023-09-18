from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_success, name='login_success'),
    path('logout/', views.logout_view, name='logout_view'),

]

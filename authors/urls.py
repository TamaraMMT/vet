from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('logout/', views.logout_view, name='logout_view'),

]

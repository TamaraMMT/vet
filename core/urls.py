from django.urls import path
from . import views

app_name = 'veterinary'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('services/', views.ServicesPageView.as_view(), name='services'),
    path('about/', views.AboutPageView.as_view(), name='about'),

]

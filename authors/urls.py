from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-post/', views.create_post, name='create_post'),
    path('post/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', views.edit_posts, name='edit_posts'),

]

from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='edit_posts'),
    path(
        'authors/delete/<pk>/',
        views.DeletePostView.as_view(),
        name='delete_post'
    ),

]

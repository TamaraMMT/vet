from django.urls import path
from authors import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'authors'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.DashboardListView.as_view(), name='dashboard'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path(
        'post/<int:pk>/edit/',
        views.EditPostView.as_view(),
        name='edit_posts'),
    path(
        'authors/delete/<pk>/',
        views.DeletePostView.as_view(),
        name='delete_post'
    ),
    path(
        'profile/<int:pk>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),

]

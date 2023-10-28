from django.urls import path, include
from authors import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter

app_name = 'authors'

router = DefaultRouter()
router.register('posts', views.AuthorPostsViewSet)


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
        name='token_verify'
    ),
    path(
        'api/register',
        views.RegisterAuthorView.as_view(),
        name='register_author'
    ),
    path('api/me/', views.WhoAmIView.as_view(), name='me'),
    path('', include(router.urls)),
]

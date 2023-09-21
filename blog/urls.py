from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='posts'),
    path('category/<int:pk>/', views.CategoryPostsListView.as_view(), name='category_posts'),   # noqa:E501
]

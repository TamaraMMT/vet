from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('category/<int:pk>/', views.CategoryPostsListView.as_view(), name='category_posts'),   # noqa:E501
]

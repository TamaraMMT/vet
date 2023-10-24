from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='posts'),
    path(
        'category/<int:pk>/',
        views.CategoryPostsListView.as_view(),
        name='category_posts'
    ),
    path(
        'api/posts/v1/',
        views.BlogAPIViewSet.as_view({'get': 'list'}),
        name='list_post'
    ),
    path(
        'api/posts/v1/<int:pk>/',
        views.BlogAPIViewSet.as_view({'get': 'retrieve'}),
        name='detail_post'
    ),

]

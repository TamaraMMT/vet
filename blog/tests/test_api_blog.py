from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from blog.models import PostBlog, Category, User
from blog.serializers import PostBlogSerializer, PostDetailSerializer
from blog.views import BlogAPIViewSet
import json


class BlogAPIViewSetTest(TestCase):
    def setUp(self):
        # Create some sample data in the database
        self.category = Category.objects.create(name='Dogs')
        self.user = User.objects.create(
            username='LolaUser', password='123Password')
        self.post1 = PostBlog.objects.create(
            title='Post 1',
            category=self.category,
            article='This is the article content 1',
            slug='slug-unique1',
            author=self.user
        )
        self.post2 = PostBlog.objects.create(
            title='Post 2',
            category=self.category,
            article='This is the article content 2',
            slug='slug-unique2',
            author=self.user
        )

    def test_list_posts(self):
        url = reverse('blog:list_post')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = response.content.decode('utf-8')
        data = json.loads(content)

        self.assertEqual(data['count'], 2)

    def test_retrieve_posts_api(self):
        # Test retrieving details of a post
        url = reverse('blog:detail_post', kwargs={'pk': self.post1.pk})
        response = self.client.get(url)

        content = response.content.decode('utf-8')
        data = json.loads(content)

        self.assertEqual(data['title'], 'Post 1')
        self.assertEqual(data['article'], 'This is the article content 1')

    def test_get_serializer_classs_api(self):
        # Test the get_serializer_class method
        view = BlogAPIViewSet()
        view.action = "list"
        serializer_class = view.get_serializer_class()
        self.assertEqual(serializer_class, PostBlogSerializer)

        view.action = "retrieve"
        serializer_class = view.get_serializer_class()
        self.assertEqual(serializer_class, PostDetailSerializer)

from django.test import TestCase
from django.urls import reverse


class BlogURLsTest(TestCase):
    def test_blog_home_url_is_correct(self):
        url = reverse('blog:blog')
        self.assertEqual(url, '/blog/')

    def test_blog_post_url_is_correct(self):
        url = reverse('blog:post', kwargs={'pk': 1})
        self.assertEqual(url, '/blog/post/1/')

    def test_blog_create_post_url_is_correct(self):
        url = reverse('blog:create_post')
        self.assertEqual(url, '/blog/create-post/')

    def test_category_post_url_is_correct(self):
        url = reverse('blog:category_posts', kwargs={'pk': 1})
        self.assertEqual(url, '/blog/category/1/')

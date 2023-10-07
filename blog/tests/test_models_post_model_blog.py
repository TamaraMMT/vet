from django.forms import ValidationError
from blog.tests.test_post_base import PostTestBase
from django.test import TestCase
from blog.models import User, Category, PostBlog


class PostModelTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        return super().setUp()

    def test_post_title_raise_error_if_title_has_more_65_chars(self):
        self.post.title = 'A' * 66
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_post_article_raise_error_if_title_has_more_65_chars(self):
        self.post.article = 'A' * 1501
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), 'My first post')


class PostBlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', first_name='Name User', password='testpassword')

        self.category = Category.objects.create(name='Example Category')

        self.post = PostBlog(
            title='Test Post',
            article='This is a test post content.',
            category=self.category,
            author=self.user
        )

    def test_get_absolute_url(self):
        self.post.save()

        expected_url = f'/blog/post/{self.post.id}/'
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_slug_generation(self):
        self.post.save()

        expected_slug = 'test-post'
        self.assertEqual(self.post.slug, expected_slug)

from django.forms import ValidationError
from blog.tests.test_post_base import PostTestBase


class PostModelTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        return super().setUp()

    def test_posts_title_raise_error_if_title_has_more_65_chars(self):
        self.post.title = 'A' * 66
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_posts_article_raise_error_if_title_has_more_65_chars(self):
        self.post.article = 'A' * 1501
        with self.assertRaises(ValidationError):
            self.post.full_clean()

    def test_posts_str_representation(self):
        self.assertEqual(str(self.post), 'My first post')


class CategoryModelTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        self.category = self.make_category(name='Category')
        return super().setUp()

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), 'Category')

    def test_category_raise_error_if_title_has_more_65_chars(self):
        self.category.name = 'A' * 61
        with self.assertRaises(ValidationError):
            self.category.full_clean()

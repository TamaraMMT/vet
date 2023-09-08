from django.test import TestCase
from blog.models import PostBlog, Category
from django.contrib.auth.models import User
import random
import string


class PostTestBase(TestCase):
    def setUp(self):
        self.post = self.make_post()
        super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username=None,
        password='123456',
        email='username@gmail.com'
    ):
        if username is None:
            username = ''.join(random.choices(string.ascii_lowercase, k=6))

        return User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

    def make_post(
            self,
            title='My first post',
            slug=None,
            article='Building a strong bond with your feline friend involves more than simply providing food and shelter. Cat training, often overlooked, can be a fulfilling endeavor that enhances your relationship. In this article, delve into the world of cat training, where patience and understanding pave the way to mutual understanding. ',
            category_data=None,
            author_data=None,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        if not slug:
            slug = ''.join(random.choices(string.ascii_lowercase, k=6))
            while PostBlog.objects.filter(slug=slug).exists():
                slug = ''.join(random.choices(string.ascii_lowercase, k=6))

        return PostBlog.objects.create(
            title=title,
            slug=slug,
            article=article,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )

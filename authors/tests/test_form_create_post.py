from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import PostBlog, Category
from django.urls import reverse


class CreatePostIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            first_name='Name User',
            password='testpassword'
        )

        self.category = Category.objects.create(name='Example Category')

        self.form_data = {
            'title': 'First Post',
            'article': 'This is the content of the first post.',
            'slug': 'first-post',
            'category': self.category.id,
            'author': self.user.id,
        }

    def test_create_post_form(self):
        # user login
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(
            reverse('authors:create_post'), data=self.form_data, follow=True)

        # Check if the post creation was successful
        self.assertEqual(response.status_code, 200)

        # Check if the post was successfully created in the database
        created_post = PostBlog.objects.get(title='First Post')
        self.assertEqual(created_post.title, 'First Post')
        self.assertEqual(created_post.article,
                         'This is the content of the first post.')
        self.assertEqual(created_post.slug, 'first-post')
        self.assertEqual(created_post.category, self.category)
        self.assertEqual(created_post.author, self.user)

    def test_create_post_form_unique_title(self):

        self.client.login(username='testuser', password='testpassword')
        url = reverse('authors:create_post')
        self.client.post(url, data=self.form_data, follow=True)

        self.form_data['title'] = 'First Post'

        response2 = self.client.post(url, data=self.form_data)
        msg = 'Title already exist'

        title_errors = response2.context['form'].errors.get('title')

        if title_errors:
            self.assertIn(msg, title_errors)

    def test_create_post_max_char_title(self):

        self.client.login(username='testuser', password='testpassword')
        url = reverse('authors:create_post')
        self.client.post(url, data=self.form_data, follow=True)

        self.form_data['title'] = 'First Post' * 100

        response2 = self.client.post(url, data=self.form_data)
        msg = 'Max 100 characters'

        title_errors = response2.context['form'].errors.get('title')

        if title_errors:
            self.assertIn(msg, title_errors)

    def test_create_post_min_char_title(self):

        self.client.login(username='testuser', password='testpassword')
        url = reverse('authors:create_post')
        self.client.post(url, data=self.form_data, follow=True)

        self.form_data['title'] = 'First P'

        response2 = self.client.post(url, data=self.form_data)
        msg = 'Minimum 10 characters'

        title_errors = response2.context['form'].errors.get('title')

        if title_errors:
            self.assertIn(msg, title_errors)

    def test_create_post_min_char_article(self):

        self.client.login(username='testuser', password='testpassword')
        url = reverse('authors:create_post')
        self.client.post(url, data=self.form_data, follow=True)

        self.form_data['article'] = 'This article...'

        response2 = self.client.post(url, data=self.form_data)
        msg = 'Minimum 20 characters'

        article_errors = response2.context['form'].errors.get('article')

        if article_errors:
            self.assertIn(msg, article_errors)

    def test_create_post_max_char_article(self):

        self.client.login(username='testuser', password='testpassword')
        url = reverse('authors:create_post')
        self.client.post(url, data=self.form_data, follow=True)

        self.form_data['article'] = 'First Post' * 1500

        response2 = self.client.post(url, data=self.form_data)
        msg = 'Max 1500 characters'

        article_errors = response2.context['form'].errors.get('article')

        if article_errors:
            self.assertIn(msg, article_errors)

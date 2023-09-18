
from django.test import TestCase
from authors.forms import LoginForm
from django.urls import reverse
from django.contrib.auth.models import User


class LoginAuthorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='password123',
        )

    def test_login_get_view_template_form_status_code(self):
        response = self.client.get(reverse('authors:login'))
        form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/pages/login.html')
        self.assertTrue(isinstance(form, LoginForm))

    def test_login_post_success_redirecr_dashboard(self):
        self.client.login(username='test_user', password='password123')
        response = self.client.get(reverse('authors:login'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('authors:dashboard'))

    def test_login_successful_authentication(self):
        url = reverse('authors:login')
        data = {
            'username': 'test_user',
            'password': 'password123',
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertRedirects(response, reverse('authors:dashboard'))
        self.assertContains(response, 'You are logged in')

    def test_login_invalid_credentials(self):
        url = reverse('authors:login')
        data = {
            'username': 'test_user',
            'password': 'password-incorrect',
        }

        response = self.client.post(url, data=data, follow=True)

        msg = 'Invalid credentials'

        self.assertContains(response, msg)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_login_invalid_fields(self):
        url = reverse('authors:login')
        data = {
            'username': 'test_user',
            'password': '',
        }

        response = self.client.post(url, data=data, follow=True)
        msg = 'Sorry! Form not sent. Check all fields.'

        self.assertContains(response, msg)

    def test_login_view_if_user_is_authenticated_redirect_dashboard(self):
        self.client.login(username='test_user', password='password123')

        response = self.client.get(reverse('authors:login'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('authors:dashboard'))


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LogoutViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_logout_view(self):
        response = self.client.get(reverse('authors:logout_view'))

        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('authors:login'))

    def test_logout_redirect_view_message(self):
        response = self.client.get(reverse('authors:logout_view'), follow=True)
        msg = 'You are logged out'

        self.assertContains(response, msg)

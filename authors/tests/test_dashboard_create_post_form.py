
from django.test import TestCase as DjangoTestCase
from blog.models import Category
from authors.forms.post_form import AuthorPostForm
from django.urls import reverse
from django.contrib.auth.models import User


class BasePostViewTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        category = Category.objects.create(name='Example Category')
        self.post = {
            'title': 'Sample Title post blog',
            'slug': 'sample-slug',
            'article': 'Nihil mollitia deleniti officia exercitationem',
            'category': category,
        }

        return super().setUp(*args, **kwargs)


class DashboardViewTest(BasePostViewTest):
    def test_dashboard_redirect_login_url_and_redirect_field_name(self):
        self.client.logout()
        response_dashboard = self.client.get(reverse('authors:dashboard'))

        self.assertEqual(response_dashboard.status_code, 302)
        self.assertRedirects(response_dashboard, reverse(
            'authors:login') + '?next=' + reverse('authors:dashboard'))

    def test_dashboard_page_contains_title(self):
        response = self.client.get(reverse('authors:dashboard'))
        context = response.context

        self.assertEqual(context['title'], 'Dashboard')


class CreatePostViewTest(BasePostViewTest):
    def test_create_post_redirect_login_url_and_redirect_field_name(self):
        self.client.logout()
        response_create_post = self.client.get(reverse('authors:create_post'))

        self.assertEqual(response_create_post.status_code, 302)
        self.assertRedirects(response_create_post, reverse(
            'authors:login') + '?next=' + reverse('authors:create_post'))

    def test_create_post_view_form_and_template(self):
        response = self.client.get(reverse('authors:create_post'))
        form = response.context['form']

        self.assertTrue(isinstance(form, AuthorPostForm))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/pages/create_post.html')

    def test_create_post_redirect_if_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('authors:create_post'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'authors:login') + '?next=' + reverse('authors:create_post'))

    def test_create_post_page_contains_title(self):
        response = self.client.get(reverse('authors:create_post'))
        context = response.context

        self.assertEqual(context['title'], 'New post')


class EditPostViewTest(BasePostViewTest):
    def test_edit_post_page_contains_title(self):
        response = self.client.get(reverse('authors:dashboard'))
        context = response.context

        self.assertEqual(context['title'], 'Dashboard')

from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from django.urls import reverse
from .models import ContactMessage

# Create your tests here.


class ContactViewTest(DjangoTestCase):
    def setUp(self):
        self.url = reverse('contact:contact')
        self.contact_form = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, this is a test message.'
        }

    def test_contact_page_status_code_get(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template_is_correct(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_page_contains_title(self):
        response = self.client.get(reverse('contact:contact'))
        context = response.context
        self.assertEqual(context['title'], 'Contact Us')

    def test_contact_page_status_code_post_and_redirect(self):
        response = self.client.post(
            reverse('contact:contact'), data=self.contact_form)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact:success_contact'))


class ContactMessageModelTest(TestCase):
    def test_str_model_contact_message(self):
        message = ContactMessage(
            name='John Doe', email='johndoe@example.com', message='Hello, world!')
        self.assertEqual(str(message), f'John Doe ({message.email})')


class ContactTestUrl(TestCase):
    def test_core_vet_contact_url_is_correct(self):
        contact_url = reverse('contact:contact')
        self.assertEqual(contact_url, '/contact/')

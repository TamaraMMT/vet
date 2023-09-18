from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm

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

    def test_contact_page_status_code_post_invalid_form(self):
        invalid_form_data = {
            'name': '',
            'email': 'invalid-email',
            'message': '',
        }
        form = ContactForm(data=invalid_form_data)

        response = self.client.post(self.url, data=invalid_form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

        self.assertIsInstance(response.context['form'], ContactForm)

        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('message', form.errors)


class ContactMessageModelTest(TestCase):
    def test_str_model_contact_message(self):
        message = ContactMessage(
            name='John Doe',
            email='johndoe@example.com',
            message='Hello, world!'
        )
        self.assertEqual(str(message), f'John Doe ({message.email})')


class ContactTestUrl(TestCase):
    def test_core_vet_contact_url_is_correct(self):

        contact_url = reverse('contact:contact')
        self.assertEqual(contact_url, '/contact/')


class ContactTestSendMessage(DjangoTestCase):
    def setUp(self):
        self.url = reverse('contact:contact')
        self.contact_form = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, this is a test message.'
        }

    def test_contact_page_status_code_post(self):
        response = self.client.post(
            reverse('contact:contact'), data=self.contact_form)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact:success_contact'))
        self.assertTrue(self.contact_form.is_valid())

    def test_contact_page_status_code_redirect(self):
        response = self.client.post(
            reverse('contact:contact'), data=self.contact_form, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('contact:success_contact'))

    def test_contact_page_status_code_post(self):
        form = ContactForm(data=self.contact_form)
        response = self.client.post(self.url, data=self.contact_form)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact:success_contact'))

        self.assertTrue(form.is_valid())

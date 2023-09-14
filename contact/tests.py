from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class ContactTestUrl(TestCase):
    def test_core_vet_contact_url_is_correct(self):
        contact_url = reverse('contact:contact')
        self.assertEqual(contact_url, '/contact/')


class ContactPageViewTest(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template_used(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_page_contains_title(self):
        response = self.client.get(reverse('contact:contact'))
        context = response.context
        self.assertEqual(context['title'], 'Contact Us')

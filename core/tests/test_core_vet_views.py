from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('veterinary:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('veterinary:home'))
        self.assertTemplateUsed(response, 'core/pages/home.html')

    def test_home_page_contains_title(self):
        response = self.client.get(reverse('veterinary:home'))
        context = response.context
        self.assertEqual(context['title'], 'Home')


class ServicesPageViewTest(TestCase):
    def test_services_page_status_code(self):
        response = self.client.get(reverse('veterinary:services'))
        self.assertEqual(response.status_code, 200)

    def test_services_page_template_used(self):
        response = self.client.get(reverse('veterinary:services'))
        self.assertTemplateUsed(response, 'core/pages/services.html')

    def test_services_page_contains_title(self):
        response = self.client.get(reverse('veterinary:services'))
        context = response.context
        self.assertEqual(context['title'], 'Services')


class ContactPageViewTest(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse('veterinary:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template_used(self):
        response = self.client.get(reverse('veterinary:contact'))
        self.assertTemplateUsed(response, 'core/pages/contact.html')

    def test_contact_page_contains_title(self):
        response = self.client.get(reverse('veterinary:contact'))
        context = response.context
        self.assertEqual(context['title'], 'Contact Us')


class AboutUsPageViewTest(TestCase):
    def test_about_page_status_code(self):
        response = self.client.get(reverse('veterinary:about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_used(self):
        response = self.client.get(reverse('veterinary:about'))
        self.assertTemplateUsed(response, 'core/pages/about.html')

    def test_about_page_contains_title(self):
        response = self.client.get(reverse('veterinary:about'))
        context = response.context
        self.assertEqual(context['title'], 'About Us')

from django.test import TestCase
from django.urls import reverse


class CoreVetURLsTest(TestCase):
    def test_core_vet_home_url_is_correct(self):
        home_url = reverse('veterinary:home')
        self.assertEqual(home_url, '/')

    def test_core_vet_services_url_is_correct(self):
        services_url = reverse('veterinary:services')
        self.assertEqual(services_url, '/services/')

    def test_core_vet_contact_url_is_correct(self):
        contact_url = reverse('veterinary:contact')
        self.assertEqual(contact_url, '/contact/')

    def test_core_vet_about_url_is_correct(self):
        about_url = reverse('veterinary:about')
        self.assertEqual(about_url, '/about/')

from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from authors.forms import RegistrationForm
from parameterized import parameterized
from django.urls import reverse
from django.contrib.auth.models import User


class AuthorRegisterFormUnittest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('first_name', 'Your first name'),
        ('last_name', 'Your last name'),
        ('email', 'Your email'),
        ('password', 'Your password'),
        ('password2', 'Repeat your password')
    ])
    def test_register_placeholder_fields_is_correct(self, field, placeholder):
        form = RegistrationForm()
        placeholder_form = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder_form, placeholder)

    @parameterized.expand([
        ('username', 'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 30 characters.'),
        ('email', 'yourname@example.com'),
        ('password', 'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'),
    ])
    def test_register_help_text_fields_is_correct(self, field, help_text):
        form = RegistrationForm()
        current = form[field].field.help_text
        self.assertEqual(current, help_text)

    @parameterized.expand([
        ('username', 'This field must not be empty'),
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name'),
        ('email', 'E-mail is required'),
        ('password', 'Password must not be empty'),
        ('password2', 'Please, repeat your password'),
    ])
    def test_register_required_fields_is_correct(self, field, error_messages):
        form = RegistrationForm()
        current = form.fields[field].error_messages['required']
        self.assertEqual(current, error_messages)


class RegisterIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'test_user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'test@example.com',
            'password': 'Str0ngP@ssword1',
            'password2': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)

    def test_register_get_view_and_template_form(self):
        response = self.client.get(reverse('authors:register'))
        form = response.context['form']

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/pages/register_view.html')
        self.assertTrue(isinstance(form, RegistrationForm))

    def test_register_post_view_with_valid_form(self):
        response = self.client.post(
            reverse('authors:register'), data=self.form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('authors:login'))

        # Check if the user was created
        user = User.objects.get(username='test_user')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.first_name, 'first')
        self.assertEqual(user.last_name, 'last')

    @parameterized.expand([
        ('username', 'This field must not be empty'),
        ('first_name', 'Write your first name'),
        ('last_name', 'Write your last name'),
        ('password', 'Password must not be empty'),
        ('password2', 'Please, repeat your password'),
        ('email', 'E-mail is required'),
    ])
    # Check if the field not is empty
    def test_register_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data)

        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_register_username_field_min_length_4_error(self):
        self.form_data['username'] = 'Lu'
        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data)
        msg = 'Minimum 4 characters'

        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_register_username_field_max_length_30_error(self):
        self.form_data['username'] = 'vet' * 31
        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data)
        msg = 'Max 30 characters'
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_password_field_have_lower_upper_case_latters_and_numbers(self):
        self.form_data['password'] = '123'
        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data)
        msg = ('Password must have at least one uppercase letter, '
               'one lowercase letter and one number. The length should be '
               'at least 8 characters.')

        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_register_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@Str0ngP@ssword1'
        self.form_data['password2'] = '@Str0ngP@ssword1dif'

        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data)

        msg = 'The passwords do not equal'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@Str0ngP@ssword1'
        self.form_data['password2'] = '@Str0ngP@ssword1'

        url = reverse('authors:register')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))

    def test_register_email_unique(self):
        url = reverse('authors:register')
        response1 = self.client.post(url, data=self.form_data, follow=True)

        self.form_data['email'] = 'test2@example.com'

        response2 = self.client.post(url, data=self.form_data)
        msg = 'User e-mail is already in use'

        email_errors = response2.context['form'].errors.get('email')

        if email_errors:
            self.assertIn(msg, email_errors)

    def test_register_view_if_user_is_authenticated_redirect(self):
        user = User.objects.create_user(
            username='test_user', password='password')

        self.client.login(username='test_user', password='password')

        response = self.client.get(reverse('authors:register'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('authors:dashboard'))

    def test_registration_page(self):
        self.client.logout()
        response = self.client.get(reverse('authors:register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/pages/register_view.html')

    def test_clean_email_already_exists(self):
        existing_email = 'test@example.com'
        User.objects.create_user(
            username='existing_user', email=existing_email, password='password')

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': existing_email,
            'password': 'StrongPass123',
            'password2': 'StrongPass123',
        }
        form = RegistrationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'][0],
                         'User e-mail is already in use')

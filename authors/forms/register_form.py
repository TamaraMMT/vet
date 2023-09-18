from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.forms_utils import strong_password


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username'}),
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 30 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 4 characters',
            'max_length': 'Max 30 characters',
        },
        min_length=4, max_length=30,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your first name'}),
        error_messages={'required': 'Write your first name'},
        label='First name'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'}),
        error_messages={'required': 'Write your last name'},
        label='Last name',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email'}),
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='yourname@example.com',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password],
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat your password'}),
        label='Password2',
        error_messages={
            'required': 'Please, repeat your password'
        },
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'The passwords do not equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })

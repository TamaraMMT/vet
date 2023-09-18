from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username'}),
        error_messages={'required': 'Write your username'},
        label='username'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Input your password'}),
        label='password'
    )

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name'}),
        label='name',
        error_messages={'required': 'This field must not be empty'},
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email'}),
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        required=True,
    )

    message = forms.CharField(
        label='message',
        widget=forms.TextInput(
            attrs={'placeholder': 'Write your message here'}),
        max_length=300,
        error_messages={'required': 'This field must not be empty'},
        required=True,
    )

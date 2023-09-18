from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name'}),
        label='name',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email'}),
        label='E-mail',
    )

    message = forms.CharField(
        label='message',
        widget=forms.TextInput(
            attrs={'placeholder': 'Write your message here'}),
        max_length=300,
    )

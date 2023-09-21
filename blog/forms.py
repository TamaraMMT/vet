from blog.models import Category, PostBlog
from django import forms


class AuthorPostForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        help_text='The length should be between 4 and 30 characters.',
        min_length=10,
        max_length=100,
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 10 characters',
            'max_length': 'Max 100 characters',
        },
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400 focus:ring-inset sm:text-sm sm:leading-6',
            'placeholder': 'Input new title',
        }),
    )

    article = forms.CharField(
        label='Article',
        help_text='The length should be between 20 and 1500 characters.',
        min_length=20,
        max_length=1500,
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 20 characters',
            'max_length': 'Max 1500 characters',
        },
        widget=forms.Textarea(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400 focus:ring-inset sm:text-sm sm:leading-6',
            'rows': 10,
        }),
    )

    slug = forms.CharField(
        label='slug',
        help_text='example-slug-title',
        error_messages={
            'required': 'This field must not be empty',

        }
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category',
        widget=forms.Select(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400 focus:ring-inset sm:text-sm sm:leading-6',
        }),
    )

    class Meta:
        model = PostBlog
        fields = 'title', 'article', 'category', 'slug', 'cover'

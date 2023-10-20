from blog.models import Category, PostBlog
from django.core.exceptions import ValidationError
from django import forms


class AuthorPostForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        min_length=10,
        max_length=100,
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 10 characters',
            'max_length': 'Max 100 characters',
        },
        widget=forms.TextInput(attrs={
            'class': 'my-3 block w-full rounded-md border-0 p-1 text-gray-900 '
                     'shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400'
                     'focus:ring-inset sm:text-sm sm:leading-6',
            'placeholder': 'Input your title',
        }),
    )

    article = forms.CharField(
        label='Article',
        min_length=20,
        max_length=1500,
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 20 characters',
            'max_length': 'Max 1500 characters',
        },
        widget=forms.Textarea(attrs={
            'class': 'my-3 block w-full rounded-md border-0 p-1 text-gray-900 '
                     'shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400'
                     'focus:ring-inset sm:text-sm sm:leading-6',
            'placeholder': 'Input your article',
            'rows': 10,
        }),
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category',
        widget=forms.Select(attrs={
            'class': 'my-3 block rounded-md border-0 p-1 text-gray-900 '
                     'shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400'
                     'focus:ring-inset sm:text-sm sm:leading-6',
        }),
    )

    slug = forms.SlugField(
        label='Slug',
        min_length=10,
        max_length=100,
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Minimum 10 characters',
            'max_length': 'Max 100 characters',
        },
        widget=forms.TextInput(attrs={
            'class': 'my-3 block w-full rounded-md border-0 p-1 text-gray-900 '
                     'shadow-sm ring-1 ring-gray-300 placeholder:text-gray-400'
                     'focus:ring-inset sm:text-sm sm:leading-6',
            'placeholder': 'Input-your-title-for-the-slug',
        }),
    )

    class Meta:
        model = PostBlog
        fields = 'title', 'slug', 'article', 'category', 'cover'

    def validate_unique_title(self):
        title = self.cleaned_data.get('title', '')
        exists = PostBlog.objects.filter(title=title).exists()

        if exists:
            raise ValidationError(
                'Title already exist', code='invalid',
            )
        return title

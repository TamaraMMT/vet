from blog.models import PostBlog
from django import forms
from django.core.exceptions import ValidationError


class AuthorPostForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = 'title', 'article', 'category', 'slug'
        category = forms.ModelChoiceField(
            PostBlog.objects.all(), empty_label='Select a category')

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class PostBlog(models.Model):
    title = models.CharField(max_length=65)
    article = models.CharField(max_length=1500)
    slug = models.SlugField(unique=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    cover = models.ImageField(
        upload_to='blog/covers/%Y/%m/%d',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        default=None
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:posts', args=(self.id,))

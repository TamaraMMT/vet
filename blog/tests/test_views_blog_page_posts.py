from ast import Delete
from django.urls import reverse
from .test_post_base import PostTestBase


class BlogPageViewTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        self.category = self.make_category()
        super().setUp()

    def test_view_blog_page_status_code(self):
        response = self.client.get(reverse('blog:blog'))
        self.assertEqual(response.status_code, 200)

    def test_view_blog_page_template_used(self):
        response = self.client.get(reverse('blog:blog'))
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_view_blog_page_contains_title(self):
        response = self.client.get(reverse('blog:blog'))
        context = response.context
        self.assertEqual(context['title'], 'Veterinary Blog')

# aqui falta o test da mensagem que mostra se nao tem post-------->>>>

    def test_view_blog_page_contain_post(self):
        self.make_post()
        response = self.client.get(reverse('blog:blog'))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.category.name)

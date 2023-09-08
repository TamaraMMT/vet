from django.urls import reverse
from .test_post_base import PostTestBase


class CreatePostViewTest(PostTestBase):
    def test_create_post_status_code(self):
        response = self.client.get(reverse('blog:create_post'))
        self.assertEqual(response.status_code, 200)

    def test_create_post_page_template_used(self):
        response = self.client.get(reverse('blog:create_post'))
        self.assertTemplateUsed(response, 'blog/create_post.html')

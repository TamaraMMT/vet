from django.urls import reverse
from .test_post_base import PostTestBase


class CategoryPostBlogViewTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        super().setUp()
        self.category = self.make_category(name='Category')

    def test_category_detail_view_status_code(self):
        url = reverse('blog:category_posts', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_blog_page_template_used(self):
        url = reverse('blog:category_posts', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/category_posts.html')

    def test_category_view_blog_page_contains_title(self):
        response = self.client.get(
            reverse('blog:category_posts', kwargs={'pk': self.category.pk})
        )
        context = response.context
        expected_title = self.category.name
        self.assertEqual(context['category'].name, expected_title)

    def test_category_view_page_load_post(self):
        response = self.client.get(
            reverse('blog:category_posts', kwargs={'pk': 2}))
        postcategory = response.context['posts_list_category']
        expected_post = self.post
        self.assertIn(expected_post, postcategory)

    def test_category_view_page_dont_load_post(self):
        response = self.client.get(
            reverse('blog:category_posts', kwargs={'pk': 5000}))
        self.assertEqual(response.status_code, 404)

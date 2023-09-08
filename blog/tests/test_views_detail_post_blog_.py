from django.urls import reverse
from .test_post_base import PostTestBase


class PostBlogDetailViewTest(PostTestBase):
    def test_post_blog_detail_view_status_code(self):
        response = self.client.get(
            reverse('blog:post', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_post_blog_detail_view_page_template_used(self):
        response = self.client.get(
            reverse('blog:post', kwargs={'pk': self.post.pk})
        )
        self.assertTemplateUsed(response, 'blog/blog-post.html')

    def test_post_blog_detail_view_context_data(self):
        response = self.client.get(
            reverse('blog:post', kwargs={'pk': self.post.pk})
        )
        self.assertTrue('post' in response.context)

    def test_post_blog_detail_view_title_in_context(self):
        response = self.client.get(
            reverse('blog:post', kwargs={'pk': self.post.pk})
        )
        self.assertTrue('title' in response.context)

    def test_post_blog_detail_contain_data_post(self):
        response = self.client.get(
            reverse('blog:post', kwargs={'pk': self.post.pk})
        )
        self.assertContains(response, self.post.title)

        context = response.context['post']
        self.assertEqual(context.pk, self.post.pk)
        self.assertEqual(context.title, self.post.title)
        self.assertEqual(context.slug, self.post.slug)
        self.assertEqual(context.article, self.post.article)
        self.assertEqual(context.category, self.post.category)
        self.assertEqual(context.author, self.post.author)

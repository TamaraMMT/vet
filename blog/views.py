from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from utils.pagination import make_pagination

from blog.models import PostBlog, Category


class BlogListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'blog_list'
    model = PostBlog
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Veterinary Blog'

        posts = self.get_queryset()
        page_obj, pagination_range = make_pagination(
            self.request,
            posts,
            self.paginate_by)

        context['blog_list'] = page_obj
        context['pagination_range'] = pagination_range

        return context

    def get_queryset(self):
        qs = PostBlog.objects.all().select_related(
            'author', 'category').order_by('-id')
        return qs


class PostDetailView(DetailView):
    model = PostBlog
    template_name = 'blog/blog_post.html'
    context_object_name = 'blog_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class CategoryPostsListView(ListView):
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts_list_category'
    paginate_by = 4

    def get_queryset(self):
        category_id = self.kwargs['pk']
        self.category = get_object_or_404(Category, pk=category_id)
        return PostBlog.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category

        posts = self.get_queryset()
        page_obj, pagination_range = make_pagination(
            self.request, posts, self.paginate_by)

        context['posts_list_category'] = page_obj
        context['pagination_range'] = pagination_range

        return context

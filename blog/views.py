from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from blog.utils.pagination import make_pagination
from django.contrib import messages

from blog.models import PostBlog, Category


class BlogListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    model = PostBlog
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Veterinary Blog'

        page_obj, pagination_range = make_pagination(
            self.request,
            self.get_queryset(),
            self.paginate_by,
            qty_pages=4
        )

        context['blog'] = page_obj
        context['pagination_range'] = pagination_range

        return context

    def get_queryset(self):
        return PostBlog.objects.all().order_by('-id')


class PostDetailView(DetailView):
    model = PostBlog
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class CreatePostView(CreateView):
    template_name = 'blog/create_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Post'
        return context

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request):
        title = request.POST['title']
        slug = request.POST['slug']
        article = request.POST['article']
        category_id = request.POST['category']
        author_id = request.user.id

        cover = request.FILES.get('cover', None)

        if not cover:
            default_cover_path = 'blog/default-image-post.jpg'
            cover = default_cover_path

        if PostBlog.objects.filter(slug=slug).exists():
            messages.error(
                request, 'Slug already exists. Please choose another slug.')
            return redirect('blog:create_post')

        post = PostBlog.objects.create(
            title=title,
            slug=slug,
            article=article,
            category_id=category_id,
            author_id=author_id,
            cover=cover,
        )
        messages.success(request, 'Sua receita foi salva com sucesso!')

        return redirect('blog:post', pk=post.pk)


class CategoryPostsListView(ListView):
    template_name = 'blog/category_posts.html'
    context_object_name = 'post_list_category'
    paginate_by = 5

    def get_queryset(self):
        category_id = self.kwargs['pk']
        self.category = get_object_or_404(Category, pk=category_id)
        return PostBlog.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category

        page_obj, pagination_range = make_pagination(
            self.request,
            self.get_queryset(),
            self.paginate_by,
            qty_pages=4
        )

        context['post_list_category'] = page_obj
        context['pagination_range'] = pagination_range

        return context

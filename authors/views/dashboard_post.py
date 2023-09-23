from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from blog.models import PostBlog, Category
from authors.forms.post_form import AuthorPostForm
from django.utils.text import slugify


class CreatePostView(LoginRequiredMixin, CreateView):
    model = PostBlog
    form_class = AuthorPostForm
    template_name = 'authors/pages/create_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = form.cleaned_data['slug']
        messages.success(self.request, 'Your post was created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error in the form.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('blog:posts', kwargs={'pk': self.object.pk})


class EditPostView(LoginRequiredMixin, UpdateView):
    model = PostBlog
    form_class = AuthorPostForm
    template_name = 'authors/pages/dashboard_edit_post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, 'Your post was created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error in the form.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('blog:posts', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = PostBlog
    form_class = AuthorPostForm
    success_url = reverse_lazy('authors:dashboard')

    def get_queryset(self):
        return PostBlog.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)

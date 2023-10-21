from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from blog.models import PostBlog, Category
from authors.forms.post_form import AuthorPostForm
from django.urls import reverse_lazy


class BasePostView(LoginRequiredMixin):
    login_url = 'authors:login'
    redirect_field_name = 'next'
    model = PostBlog
    form_class = AuthorPostForm
    context_object_name = 'posts'
    success_url_name = 'blog:posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = self.page_title
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error in the form.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy(
            self.success_url_name,
            kwargs={'pk': self.object.pk}
        )


class DashboardListView(BasePostView, ListView):
    template_name = 'authors/pages/dashboard.html'
    paginate_by = 6
    page_title = 'Dashboard'

    def get_queryset(self):
        return PostBlog.objects.filter(
            author=self.request.user
        ).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()

        return context


class CreatePostView(BasePostView, CreateView):
    template_name = 'authors/pages/create_post.html'
    success_message = 'Your post was created!'
    page_title = 'New post'


class EditPostView(BasePostView, UpdateView):
    template_name = 'authors/pages/dashboard_edit_post.html'
    success_message = 'Your post was edited!'
    page_title = 'Edit post'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


class DeletePostView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('authors:dashboard')

    def get_queryset(self):
        return PostBlog.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)

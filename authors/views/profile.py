from django.views.generic import TemplateView
from authors.models import Profile
from django.shortcuts import get_object_or_404


class ProfileView(TemplateView):
    template_name = 'authors/pages/profile_authors.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        profile_pk = context.get('pk')
        profile = get_object_or_404(Profile.objects.filter(
            pk=profile_pk
        ).select_related('author'), pk=profile_pk)

        return self.render_to_response({
            **context,
            'profile': profile,
        })

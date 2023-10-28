
""" Views for post authors"""

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import PostBlog

from authors.serializers import (
    RegistrationAuthorSerializer,
    PostBlogAuthorSerializer
)


class RegisterAuthorView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = RegistrationAuthorSerializer


class AuthorPostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostBlogAuthorSerializer
    queryset = PostBlog.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve posts for the authenticated user"""
        return PostBlog.objects.filter(
            author=self.request.user
        ).order_by('-id')

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(author=self.request.user)

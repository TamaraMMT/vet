
""" Views for post authors"""

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
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
        queryset = PostBlog.objects.filter(
            author=self.request.user
        ).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(author=self.request.user)


class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'last_login': request.user.last_login.strftime("%Y-%m-%d %H:%M:%S")
            if request.user.last_login else None,
        }
        return Response(user_data)

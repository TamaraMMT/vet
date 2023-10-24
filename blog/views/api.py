

from rest_framework import viewsets

from blog.models import PostBlog
from blog.serializers import (
    PostBlogSerializer,
    PostDetailSerializer
)


class BlogAPIViewSet(viewsets.ModelViewSet):
    queryset = PostBlog.objects.all()
    serializer_class = PostBlogSerializer  # Set a default serializer class

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return self.serializer_class

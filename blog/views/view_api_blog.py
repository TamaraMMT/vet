
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,

)
from rest_framework import viewsets

from blog.models import PostBlog
from blog.serializers import (
    PostBlogSerializer,
    PostDetailSerializer
)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'categorys',
                OpenApiTypes.INT,
                description='Category IDs to filter',
            ),
        ]
    )
)
class BlogAPIViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostBlogSerializer
    queryset = PostBlog.objects.all()

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categorys')
        if category_id:
            queryset = PostBlog.objects.filter(
                category__id=category_id)
        else:
            queryset = super().get_queryset()
        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        return self.serializer_class

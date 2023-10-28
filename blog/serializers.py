"""
Serializers for Blog APIs
"""

from rest_framework.serializers import ModelSerializer

from blog.models import Category, PostBlog
from authors.serializers import UserSerializer


class CategorySerializer(ModelSerializer):
    """Serializer for category"""
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class PostBlogSerializer(ModelSerializer):
    """Serializer for posts"""
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = PostBlog
        fields = ['id', 'title', 'author', 'category']


class PostDetailSerializer(PostBlogSerializer):
    """Serializer for post detail view"""

    class Meta(PostBlogSerializer.Meta):
        fields = PostBlogSerializer.Meta.fields + \
            ['article', 'slug', 'update_ad', 'created_ad']

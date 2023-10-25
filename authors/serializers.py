"""
Serializers for the user API
"""

from django.contrib.auth import (
    authenticate,
)
from blog.models import (
    User,
)

from blog.models import PostBlog
from django.utils.translation import gettext as _
from rest_framework import serializers
from utils.forms_utils import strong_password


class RegistrationSerializer(serializers.ModelSerializer):
    """ The fields from your registration form """
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(
        write_only=True,
        validators=[strong_password],
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'password2']

    def validate(self, data):
        """ Perform custom validation """
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("The passwords do not match.")

        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User email is already in use.")

        return data

    def create(self, validated_data):
        """ Create a new user instance with the validated data"""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user """
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class PostBlogAuthorSerializer(serializers.ModelSerializer):
    """Serializer for Authors posts """
    class Meta:
        model = PostBlog
        fields = ['id', 'title', 'slug', 'article', 'author', 'category']
        read_only_fields = ['id', 'author']

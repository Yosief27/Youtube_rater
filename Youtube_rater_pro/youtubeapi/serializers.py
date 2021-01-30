from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers
from.models import Video, Rating


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # we need to add all the fields and the methods of the model we need to be serialized
        fields = ('id', 'title', 'description', 'rating_average',
                  'url', 'category', 'subcategory', 'author', 'comments_list')
        extra_kwargs = {'url': {'required': True}}


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'video', 'comments')
        extra_kwargs = {'stars': {'required': True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        Token.objects.create(user=user)
        return user

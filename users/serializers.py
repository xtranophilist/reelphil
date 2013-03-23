from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SimpleProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()

    class Meta:
        model = Profile
        fields = ('user',)


class ProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    followers = SimpleProfileSerializer()
    following = SimpleProfileSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'full_name', 'followers', 'following')

from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SimpleProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    # username = serializers.Field(source='user.username')

    class Meta:
        model = Profile
        fields = ('user',)


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user',)


class ProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    followers = SimpleProfileSerializer()
    # following = SimpleProfileSerializer()
    # followers_set = serializers.Field()
    # following = FollowingSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'full_name')
        # deptj

# ProfileSerializer.base_fields['following'] = FollowingSerializer()


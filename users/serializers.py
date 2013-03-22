from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User


class WebUserSerializer(serializers.Serializer):
    id = serializers.Field()
    username = serializers.Field()
    email = serializers.Field()

    class Meta:
        model = User
        fields = ('id', 'username')


class SimpleProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    # username = serializers.Field(source='user.username')

    class Meta:
        model = Profile
        fields = ('user',)


class ProfileSerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    followers = SimpleProfileSerializer()
    following = SimpleProfileSerializer()
    # followers = serializers.ManyRelatedField()

    class Meta:
        model = Profile
        fields = ('user', 'full_name', 'followers')

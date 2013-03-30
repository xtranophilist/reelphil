from movie.models import Movie, ItemList, Person, Activity
from rest_framework import serializers
from users.serializers import WebUserSerializer


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'slug')


class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug')


class MovieSerializer(serializers.ModelSerializer):
    user_data = serializers.Field()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug', 'user_data')


class FullListSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField()
    items = MovieSerializer()

    class Meta:
        model = ItemList
        fields = ('name', 'description', 'author', 'items')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ('name', 'description', 'slug')


class FullMovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True)
    list_items = ListSerializer(many=True)
    user_data = serializers.Field()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug', 'directors', 'user_data', 'list_items', 'rating', 'runtime')


class FullPersonSerializer(serializers.ModelSerializer):
    directions = MovieSerializer(many=True)

    class Meta:
        model = Person
        fields = ('name', 'slug', 'directions')


class ActivitySerializer(serializers.ModelSerializer):
    user = WebUserSerializer()
    movie = SimpleMovieSerializer()
    act = serializers.Field(source='activity_type')

    class Meta:
        model = Activity
        fields = ('id', 'user', 'movie', 'act', 'timestamp')

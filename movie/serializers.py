from movie.models import Movie, ItemList, Person, MovieUser
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'slug')


class MovieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieUser
        fields = ('watched', 'owned', 'liked', 'disliked', 'favorited')


class MovieSerializer(serializers.ModelSerializer):
    watched = serializers.BooleanField()
    owned = serializers.BooleanField()
    user_data = MovieUserSerializer()

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
    watched = serializers.BooleanField()
    owned = serializers.BooleanField()
    user_data = MovieUserSerializer()
    list_items = ListSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug', 'directors', 'user_data', 'list_items')


class FullPersonSerializer(serializers.ModelSerializer):
    directions = MovieSerializer(many=True)

    class Meta:
        model = Person
        fields = ('name', 'slug', 'directions')


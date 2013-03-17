from movie.models import Movie, ItemList, Person, MovieUser
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'slug')


class MovieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieUser
        fields = ('watched', 'owned')


class MovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True)
    watched = serializers.BooleanField()
    owned = serializers.BooleanField()
    user_data = MovieUserSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug', 'directors', 'user_data')


class ListSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField()
    items = MovieSerializer()

    class Meta:
        model = ItemList
        fields = ('name', 'description', 'author', 'items')

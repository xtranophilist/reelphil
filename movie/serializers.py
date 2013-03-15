from movie.models import Movie, ItemList, Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'slug')


class MovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True)
    watched = serializers.BooleanField()
    owned = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'slug', 'directors', 'watched', 'owned')


class ListSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField()
    items = MovieSerializer(many=True)

    class Meta:
        model = ItemList
        fields = ('name', 'description', 'author', 'items')

from movie.models import Movie, ItemList, Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'slug')


class MovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'year', 'slug', 'directors')


class ListSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField()
    items = MovieSerializer(many=True)

    class Meta:
        model = ItemList
        fields = ('name', 'description', 'author', 'items')

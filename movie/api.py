from tastypie.resources import ModelResource
from movie.models import Movie, ItemList


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        detail_uri_name = 'slug'

    def determine_format(self, request):
        return 'application/json'

class ListResource(ModelResource):
    class Meta:
        queryset = ItemList.objects.all()
        resource_name = 'list'
        detail_uri_name = 'slug'

    def determine_format(self, request):
        return 'application/json'

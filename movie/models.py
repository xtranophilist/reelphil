from django.db import models
from person.models import Person


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    directors = models.ManyToManyField(Person, related_name='directions')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = u'movie'


class MovieInfo(models.Model):
    movie = models.ForeignKey(Movie)
    title_type = models.IntegerField(default=1, blank=True)

    class Meta:
        db_table = u'movie_info'

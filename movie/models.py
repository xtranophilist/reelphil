from django.db import models
from person.models import Person
from django.contrib.auth.models import User
# from checkin.models import Movie_User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    directors = models.ManyToManyField(Person, related_name='directions')
    users = models.ManyToManyField(User, through='MovieUser', related_name='user_data')

    def __unicode__(self):
        return self.title + ' (' + str(self.year) + ')'

    class Meta:
        db_table = u'movie'


class MovieInfo(models.Model):
    movie = models.ForeignKey(Movie)
    title_type = models.IntegerField(default=1, blank=True)

    class Meta:
        db_table = u'movie_info'


class MovieUser(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    owned = models.BooleanField()
    liked = models.BooleanField()
    disliked = models.BooleanField()
    favorited = models.BooleanField()
    watched = models.BooleanField()

    class Meta:
        db_table = u'movie_user'

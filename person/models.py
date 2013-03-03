from django.db import models


class Person(models.Model):
    import movie.models
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    slug = models.CharField(max_length=255)
    directions = models.ManyToManyField(movie.models.Movie, through='Direction', related_name='member')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'person'


class Direction(models.Model):
    import movie.models
    movie = models.ForeignKey(movie.models.Movie, primary_key=True)
    person = models.ForeignKey(Person)
    person_name = models.CharField(max_length=765)

    def __unicode__(self):
        return self.person_name

    class Meta:
        db_table = u'movie_nm_director'
        unique_together = (("movie", "person"),)

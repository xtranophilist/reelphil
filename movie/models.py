from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = u'movie'


class MovieInfo(models.Model):
    move_id = models.ForeignKey(Movie)
    title_type = models.IntegerField()

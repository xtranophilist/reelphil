from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(max_length=4)
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)

    def __unicode__(self):
        return self.title

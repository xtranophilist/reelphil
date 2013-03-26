from django.db import models
from django.contrib.auth.models import User
from reelphil.middlewares import ThreadLocal as tl


def timestamp_or_none(user, i, movie):
    try:
        return str(Activity.objects.get(user=user, activity_type=i, movie=movie).timestamp)
    except Activity.DoesNotExist:
        return None


class Person(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'person'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    directors = models.ManyToManyField(Person, related_name='directions')
    # users = models.ManyToManyField(User, through='MovieUser', related_name='movie_user_data')

    def get_user_data(self):
        current_user = tl.get_current_user()
        if current_user.id:
            activities = {1: 'owned', 2: 'watched', 3: 'liked', 4: 'disliked', 5: 'favorited'}
            return dict((activities[i], timestamp_or_none(user=current_user, i=i, movie=self)) for i in range(1, 6))
        return None

    user_data = property(get_user_data)

    def __unicode__(self):
        return self.title + ' (' + str(self.year) + ')'

    def checkin(self, user):
        activity = Activity(movie=self, user=user, activity_type=6)
        activity.save()

    class Meta:
        db_table = u'movie'


class Activity(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    activity_type = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'activity'
        unique_together = (('movie', 'user', 'activity_type'),)


class MovieInfo(models.Model):
    movie = models.ForeignKey(Movie)
    title_type = models.IntegerField(default=1, blank=True)

    class Meta:
        db_table = u'movie_info'


class Checkin(models.Model):
    user = models.ForeignKey(User)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    checktime = models.DateTimeField(auto_now_add=True)

    def movie(self):
        return Movie.objects.get(id=self.item_id)

    class Meta:
        db_table = u'checkin'


class ItemList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Movie, through='ListItem', related_name='list_items')
    slug = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'list'


class ListItem(models.Model):
    movie = models.ForeignKey(Movie)
    item_list = models.ForeignKey(ItemList)
    description = models.TextField()

    class Meta:
        db_table = u'list_item'

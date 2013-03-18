from django.db import models
from django.contrib.auth.models import User
from reelphil.middlewares import ThreadLocal as tl
# from reelphil


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
    users = models.ManyToManyField(User, through='MovieUser', related_name='movie_user_data')

    def get_user_data(self):
        current_user = tl.get_current_user()
        if current_user.id:
            movie_user = MovieUser.objects.get(movie=self, user=current_user)
            return movie_user
        return None

    user_data = property(get_user_data)

    def __unicode__(self):
        return self.title + ' (' + str(self.year) + ')'

    class Meta:
        db_table = u'movie'


class MovieUser(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    owned = models.BooleanField()
    liked = models.BooleanField()
    disliked = models.BooleanField()
    favorited = models.BooleanField()
    watched = models.BooleanField()

    # def __init__(self, *args, **kwargs):
    #     super(MovieUser, self).__init__(*args, **kwargs)
    #     self.__original_values = {'owned': self.owned, 'liked': self.liked, 'disliked': self.disliked, 'favorited': self.favorited, 'watched': self.watched}

    # def save(self):
    #     print self.__original_values
    #     instance = super(MovieUser, self)
    #     print self.liked
    #     instance.save()
    #     return instance

    class Meta:
        db_table = u'movie_user'


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

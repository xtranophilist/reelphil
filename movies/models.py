from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)

    def __repr__(self):
        return self.name

    class Meta:
        db_table = u'person'


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    year = models.TextField()  # This field type is a guess.
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    directors = models.ManyToManyField(Person, through='Direction')

    class Meta:
        db_table = u'movie'


class Direction(models.Model):
    movie = models.ForeignKey(Movie, primary_key=True)
    person = models.ForeignKey(Person)
    person_name = models.CharField(max_length=765)

    class Meta:
        db_table = u'movie_nm_director'
        unique_together = (("movie", "person"),)


# class Genre(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)

#     class Meta:
#         db_table = u'genre'


# class List(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField()
#     description = models.TextField(blank=True)
#     image = models.TextField(blank=True)
#     author = models.IntegerField()
#     source = models.TextField(blank=True)

#     class Meta:
#         db_table = u'list'




# class MovieInfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     movie = models.ForeignKey(Movie)
#     type = models.IntegerField()

#     class Meta:
#         db_table = u'movie_info'


# class MovieRatings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     movie = models.ForeignKey(Movie)
#     imdb_votes = models.IntegerField()

#     class Meta:
#         db_table = u'movie_ratings'


# class Show(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     year = models.TextField()  # This field type is a guess.
#     year_end = models.TextField(blank=True)  # This field type is a guess.
#     rating = models.IntegerField()
#     runtime = models.IntegerField()
#     slug = models.CharField(max_length=765)

#     class Meta:
#         db_table = u'show'


# class ShowInfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     show = models.ForeignKey(Show)
#     type = models.IntegerField()

#     class Meta:
#         db_table = u'show_info'


# class Episode(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765, blank=True)
#     show = models.ForeignKey(Show)
#     year = models.TextField()  # This field type is a guess.
#     season = models.IntegerField()
#     episode = models.IntegerField()
#     rating = models.FloatField(null=True, blank=True)
#     runtime = models.IntegerField(null=True, blank=True)
#     slug = models.CharField(max_length=765)

#     class Meta:
#         db_table = u'episode'


# class EpisodeRatings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     episode = models.ForeignKey(Episode)
#     imdb_votes = models.IntegerField()

#     class Meta:
#         db_table = u'episode_ratings'


# class ShowRatings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     show_id = models.IntegerField()
#     imdb_votes = models.IntegerField()

#     class Meta:
#         db_table = u'show_ratings'


# class Soundtrack(models.Model):
#     id = models.IntegerField()
#     title = models.CharField(max_length=765)
#     lyricist = models.CharField(max_length=765, blank=True)
#     musician = models.CharField(max_length=765, blank=True)
#     performer = models.CharField(max_length=765, blank=True)
#     from_field = models.CharField(max_length=765, db_column='from', blank=True)  # Field renamed because it was a Python reserved word.
#     from_category = models.CharField(max_length=765, blank=True)
#     translator = models.CharField(max_length=765, blank=True)
#     translation_language = models.CharField(max_length=765, blank=True)
#     publisher = models.CharField(max_length=765, blank=True)

#     class Meta:
#         db_table = u'soundtrack'

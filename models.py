# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class Episode(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765, blank=True)
    show = models.ForeignKey(Show)
    year = models.TextField() # This field type is a guess.
    season = models.IntegerField()
    episode = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    class Meta:
        db_table = u'episode'

class EpisodeNmDirector(models.Model):
    episode = models.ForeignKey(Episode, primary_key=True)
    person = models.ForeignKey(Person)
    class Meta:
        db_table = u'episode_nm_director'

class EpisodeRatings(models.Model):
    id = models.IntegerField(primary_key=True)
    episode = models.ForeignKey(Episode)
    imdb_votes = models.IntegerField()
    class Meta:
        db_table = u'episode_ratings'

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'genre'

class List(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    author = models.IntegerField()
    source = models.TextField(blank=True)
    class Meta:
        db_table = u'list'

class ListNmMovie(models.Model):
    list = models.ForeignKey(List, primary_key=True)
    movie = models.ForeignKey(Movie)
    class Meta:
        db_table = u'list_nm_movie'

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    year = models.TextField() # This field type is a guess.
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    slug = models.CharField(max_length=765)
    class Meta:
        db_table = u'movie'

class MovieInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie)
    type = models.IntegerField()
    class Meta:
        db_table = u'movie_info'

class MovieNmDirector(models.Model):
    movie = models.ForeignKey(Movie, primary_key=True)
    person = models.ForeignKey(Person)
    person_name = models.CharField(max_length=765)
    class Meta:
        db_table = u'movie_nm_director'

class MovieNmGenre(models.Model):
    movie = models.ForeignKey(Movie, primary_key=True)
    genre = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'movie_nm_genre'

class MovieRatings(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie)
    imdb_votes = models.IntegerField()
    class Meta:
        db_table = u'movie_ratings'

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    slug = models.CharField(max_length=765)
    class Meta:
        db_table = u'person'

class RegistrationRegistrationprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    activation_key = models.CharField(max_length=120)
    class Meta:
        db_table = u'registration_registrationprofile'

class Show(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    year = models.TextField() # This field type is a guess.
    year_end = models.TextField(blank=True) # This field type is a guess.
    rating = models.IntegerField()
    runtime = models.IntegerField()
    slug = models.CharField(max_length=765)
    class Meta:
        db_table = u'show'

class ShowInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    show = models.ForeignKey(Show)
    type = models.IntegerField()
    class Meta:
        db_table = u'show_info'

class ShowNmGenre(models.Model):
    show_id = models.IntegerField(primary_key=True)
    genre = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'show_nm_genre'

class ShowRatings(models.Model):
    id = models.IntegerField(primary_key=True)
    show_id = models.IntegerField()
    imdb_votes = models.IntegerField()
    class Meta:
        db_table = u'show_ratings'

class SocialAuthAssociation(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=765, unique=True)
    handle = models.CharField(max_length=765, unique=True)
    secret = models.CharField(max_length=765)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=192)
    class Meta:
        db_table = u'social_auth_association'

class SocialAuthNonce(models.Model):
    id = models.IntegerField(primary_key=True)
    server_url = models.CharField(max_length=765, unique=True)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=120, unique=True)
    class Meta:
        db_table = u'social_auth_nonce'

class SocialAuthUsersocialauth(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    provider = models.CharField(max_length=96, unique=True)
    uid = models.CharField(max_length=765, unique=True)
    extra_data = models.TextField()
    class Meta:
        db_table = u'social_auth_usersocialauth'

class Soundtrack(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=765)
    lyricist = models.CharField(max_length=765, blank=True)
    musician = models.CharField(max_length=765, blank=True)
    performer = models.CharField(max_length=765, blank=True)
    from_field = models.CharField(max_length=765, db_column='from', blank=True) # Field renamed because it was a Python reserved word.
    from_category = models.CharField(max_length=765, blank=True)
    translator = models.CharField(max_length=765, blank=True)
    translation_language = models.CharField(max_length=765, blank=True)
    publisher = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'soundtrack'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=765)
    migration = models.CharField(max_length=765)
    applied = models.DateTimeField()
    class Meta:
        db_table = u'south_migrationhistory'

class UsersProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    full_name = models.CharField(max_length=600)
    class Meta:
        db_table = u'users_profile'


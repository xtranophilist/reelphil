from django.db import models
from django.contrib.auth.models import User
from movie.models import Checkin


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), {'username': self.user.username})
    get_absolute_url = models.permalink(get_absolute_url)

    def get_checkins(self):
        checkins = Checkin.objects.filter(user=self.user)
        return checkins

    checkins = property(get_checkins)

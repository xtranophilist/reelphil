from django.db import models
from django.contrib.auth.models import User
# from movie.models import Movie


class Checkin(models.Model):
    user = models.ForeignKey(User)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    checktime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'checkin'

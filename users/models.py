from django.db import models
from django.contrib.auth.models import User
import os


def get_image_path(instance, filename):
    return os.path.join('uploads/profile_images', str(instance.id), filename)


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), {'username': self.user.username})
    get_absolute_url = models.permalink(get_absolute_url)


from social_auth.signals import socialauth_registered


def new_users_handler(sender, user, response, details, **kwargs):
    profile = Profile(user=user)
    profile.full_name = details.get('fullname')
    profile.save()

    # user.is_new = True
    # if user.is_new:
    #     if "id" in response:

    #         from urllib2 import urlopen, HTTPError
    #         from django.template.defaultfilters import slugify
    #         from django.core.files.base import ContentFile

    #         try:
    #             url = None
    #             if sender == FacebookBackend:
    #                 url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
    #             elif sender == google.GoogleOAuth2Backend and "picture" in response:
    #                 url = response["picture"]

    #             if url:
    #                 avatar = urlopen(url)
    #                 profile = Profile(user=user)

    #                 profile.profile_photo.save(slugify(user.username + " social") + '.jpg', ContentFile(avatar.read()))

    #                 profile.save()

    #         except HTTPError:
    #             pass

    return False

socialauth_registered.connect(new_users_handler, sender=None)

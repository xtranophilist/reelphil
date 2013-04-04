from django.db import models
from django.contrib.auth.models import User
import os


def get_image_path(instance, filename):
    return os.path.join('static/uploads/profile_images', str(instance.id), filename)


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    profile_image = models.ImageField('Profile Image', upload_to=get_image_path, blank=True, null=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), {'username': self.user.username})
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return unicode(self.user)


from social_auth.signals import socialauth_registered
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends import google


def new_users_handler(sender, user, response, details, **kwargs):
    profile = Profile(user=user)
    profile.full_name = details.get('fullname')

    # img_url = 'http://graph.facebook.com/' + response['id'] + '/picture?type=square'
    # from django.core.files import File
    # from django.core.files.temp import NamedTemporaryFile
    # import urllib2
    # import time

    # img_temp = NamedTemporaryFile(delete=True)
    # img_temp.write(urllib2.urlopen(img_url).read())
    # img_temp.flush()

    # img_filename = profile.id+int(time.time())+'.jpg'

    # profile.profile_image.save(img_filename, File(img_temp))

    user.is_new = True
    if user.is_new:
        if "id" in response:

            from urllib2 import urlopen, HTTPError
            from django.template.defaultfilters import slugify
            from django.core.files.base import ContentFile

            try:
                url = None
                if sender == FacebookBackend:
                    url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
                elif sender == google.GoogleOAuth2Backend and "picture" in response:
                    url = response["picture"]

                if url:
                    avatar = urlopen(url)
                    profile.profile_image.save(slugify(user.username + " social") + '.jpg', ContentFile(avatar.read()))

                    profile.save()

            except HTTPError:
                pass

    return True

socialauth_registered.connect(new_users_handler, sender=None)

# from social_auth.signals import pre_update
# from social_auth.backends.facebook import FacebookBackend


# def facebook_extra_values(sender, user, response, details, **kwargs):
#     print 'wtttt'

# pre_update.connect(facebook_extra_values, sender=FacebookBackend)

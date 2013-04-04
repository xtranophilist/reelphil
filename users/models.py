from django.db import models
from django.contrib.auth.models import User
import os


def get_image_path(instance, filename):
    return os.path.join('static/uploads/profile_images', filename)


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    profile_image = models.ImageField('Profile Image', upload_to=get_image_path, blank=True, null=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), {'username': self.user.username})
    get_absolute_url = models.permalink(get_absolute_url)

    def set_profile_image_from_url(self, url):
        from urllib2 import urlopen
        from django.template.defaultfilters import slugify
        from django.core.files.base import ContentFile
        import time
        self.profile_image.save(slugify(self.user.username + str(int(time.time()))) + '.jpg', ContentFile(urlopen(url).read()))
        self.save()

    def __unicode__(self):
        return unicode(self.user)


from social_auth.signals import socialauth_registered
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends import google
from social_auth.backends.twitter import TwitterBackend


def new_users_handler(sender, user, response, details, **kwargs):

    profile = Profile(user=user)
    profile.full_name = details.get('fullname')

    # http://api.twitter.com/1/users/profile_image/details['screen_name'].json?size=original

    user.is_new = True
    if user.is_new:
        if "id" in response:
            print response

            from urllib2 import HTTPError

            try:
                url = None
                if sender == FacebookBackend:
                    url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
                elif sender == google.GoogleOAuth2Backend and "picture" in response:
                    url = response["picture"]
                if sender == TwitterBackend:
                    url = "http://api.twitter.com/1/users/profile_image/%s.json?size=original" % response["screen_name"]

                if url:
                    profile.set_profile_image_from_url(url)
                    pass

            except HTTPError:
                pass
    profile.save()
    return True

socialauth_registered.connect(new_users_handler, sender=None)

# from social_auth.signals import pre_update
# from social_auth.backends.facebook import FacebookBackend


# def facebook_extra_values(sender, user, response, details, **kwargs):
#     print 'wtttt'

# pre_update.connect(facebook_extra_values, sender=FacebookBackend)

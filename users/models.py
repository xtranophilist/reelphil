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
        return '/user/'+unicode(self.user)
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


def createUserProfile(sender, user, request, **kwargs):
        print "creating profile"
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            profile.save()

from registration.signals import user_registered
user_registered.connect(createUserProfile)

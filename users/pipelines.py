# from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

# from social_auth.models import UserSocialAuth
# from social_auth.exceptions import AuthException
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.google import GoogleBackend
from social_auth.backends.twitter import TwitterBackend

from users.models import Profile


def create_profile(backend, details, response, social_user, uid, user, *args, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user, defaults={'full_name': details.get('fullname')})
    if created:
        profile.save()
    # if backend.__class__ == GoogleBackend:
    #     user.username = details.get('email').split('@', 1)[0]
    #     user.save()


def get_user_avatar(backend, details, response, social_user, uid, user, *args, **kwargs):
    profile = user.get_profile()

    if profile.profile_image:
        return

    from urllib2 import HTTPError

    print backend.__class__

    try:
        url = None
        if backend.__class__ == FacebookBackend:
            url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
        elif backend.__class__ == GoogleBackend:
            username = details.get('email').split('@', 1)[0]
            url = "http://profiles.google.com/s2/photos/profile/%s" % username
            print url
        if backend.__class__ == TwitterBackend:
            url = "http://api.twitter.com/1/users/profile_image/%s.json?size=original" % response["screen_name"]

        if url:
            profile.set_profile_image_from_url(url)
            pass

    except HTTPError:
        pass
    profile.save()

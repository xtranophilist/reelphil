# from movie.models import Activity
# from django.db.models import Q


# class Timeline:

#     def __init__(self, user, **kwargs):
#         self.user = user
#         self.num = kwargs.get('num', 10)
#         self.type = kwargs.get('type', 'friends')
#         if self.type is 'friends':
#             # TODO single db query http://stackoverflow.com/questions/8825249/django-selecting-distinct-field-not-working
#             followings = [following.user for following in self.user.get_profile().following.all()]
#             self.activities = Activity.objects.filter(Q(user__in=followings) | Q(user=self.user)).order_by('-timestamp')
#             self.checkins = Checkin.objects.filter(Q(user__in=followings) | Q(user=self.user)).order_by('-timestamp')
#             print self.activities
#             print self.checkins

#     # @property
#     # def feeds(self):
#     #     items = []
#     #     for checkin in self.checkins:

#     #         items.append(['user' = checkin.user, 6, checkin.movie, checkin.timestamp, checkin.message])
#     #     for activity in self.activities:
#     #         items.append([activity.user, activity.activity_type, activity.movie, activity.timestamp])
#     #     print items

#     def get_recent_activity(self):
#         activities = Activity.objects.filter(user=self.user).order_by('-id')[:self.num]
#         all_activities = []
#         for activity in activities:
#             act = {1: 'owned', 2: 'watched', 3: 'liked', 4: 'disliked', 5: 'favorited'}[activity.activity_type]
#             time = activity.timestamp
#             item = activity.movie
#             all_activities.append([act, item, time])
#         checkins = Checkin.objects.filter(user=self.user).order_by('-id')[:self.num]
#         for checkin in checkins:
#             act = 'checked-in to'
#             time = checkin.checktime
#             item = checkin.movie
#             all_activities.append([act, item, time])
#         return all_activities


# class FeedItem:

#     def __init__(self, user, act, timestamp):
#         self.user = user
#         self.act = act
#         self.timestamp = timestamp

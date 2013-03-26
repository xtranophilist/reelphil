# from movie.models import Activity


# class Timeline:

#     def __init__(self, user, num=10):
#         self.user = user
#         self.num = num

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

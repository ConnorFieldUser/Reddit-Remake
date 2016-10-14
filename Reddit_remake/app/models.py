from django.db import models
from django.contrib.auth.models import User

# from django.dispatch import reciever
from datetime import datetime, timedelta


# from django.db.models.signal import post_save
# Create your models here.


class Subreddit(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    creation_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def current_count(self):
        return Post.objects.filter(post_to_subreddit=self).count()

    # # method called current_count that returns how many posts
    def today_count(self):
        hrs24 = datetime.now() - timedelta(days=1)
        return Post.objects.filter(post_to_subreddit=self).filter(creation_time__gte=hrs24).count()
    # # method called today_count that returns posts in the last 24 hours

    def daily_average(self):
        hrs24 = datetime.now() - timedelta(days=1)
        return Post.objects.filter(post_to_subreddit=self).filter(creation_time__gte=hrs24).count()/7


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    url = models.URLField(max_length=200, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    post_to_subreddit = models.ForeignKey(Subreddit)
    post_to_user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def is_recent(self):
        hrs24 = datetime.now() - timedelta(days=1)
        if Post.objects.filter(creation_time__gte=hrs24):
            return True
        else:
            return False

    def is_hot(self):
        hrs78 = datetime.now() - timedelta(days=3)
        if Comment.objects.filter(comment_to_post=self).filter(created_time__gt=hrs78).count() > 3:
            return True
        else:
            return False

        class Meta:
            ordering = ('-creation_time')


class Comment(models.Model):

    comment_text = models.CharField(max_length=255)

    comment_to_user = models.ForeignKey(User)
    comment_to_post = models.ForeignKey(Post)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} posted in '{}'".format(self.comment_to_user.username, self.comment_to_post.title)


# class Profile(models.Model):
#
#     user = models.OneToOneField('auth.User')
#     fav_snack = models.CharField(max_length=25)
#
#     @reciever(post_save, sender='auth.User')
#     def creae_user_profile(**kwargs):
#         created = kwargs.get('created')
#         instance = kwargs.get('instance')
#         if created:
#             Profile.objects.create(user=instance)

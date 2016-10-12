from django.contrib import admin

from app.models import Subreddit, Post, Comment

# Register your models here.

admin.site.register(Subreddit)
admin.site.register(Post)
admin.site.register(Comment)

from django.shortcuts import render
from app.models import Subreddit, Post, Comment

# Create your views here.


def index_view(request):
    context = {
        "subreddits": Subreddit.objects.all(),
        "junkvar": Subreddit.objects.get(id=1),
        "posts": Post.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, 'index.html', context)

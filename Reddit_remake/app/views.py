from django.shortcuts import render

from app.models import Subreddit, Post, Comment

from django.views.generic import DetailView

# Create your views here.


def index_view(request):
    context = {
        "subreddits": Subreddit.objects.all(),
        "junkvar": Subreddit.objects.get(id=1),
        "posts": Post.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, 'index.html', context)


def testing_view(request):
    context = {
        "subreddits": Subreddit.objects.all(),
        "junkvar": Subreddit.objects.get(id=1),
        "posts": Post.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, 'testing.html', context)


def subreddits_view(request):
    context = {
        "subreddits": Subreddit.objects.all(),
    }
    return render(request, "subreddits.html", context)


class SubredditDetailView(DetailView):
    queryset = Subreddit.objects.all().order_by("-creation_time")

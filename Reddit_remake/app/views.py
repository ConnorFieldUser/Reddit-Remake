from django.shortcuts import render

from app.models import Subreddit, Post, Comment

from django.views.generic import DetailView
from django.views.generic.edit import CreateView  # UpdateView

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

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
        "junkvar": Subreddit.objects.get(id=2),
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
    model = Subreddit


class PostDetailView(DetailView):
    model = Post


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/subreddits"

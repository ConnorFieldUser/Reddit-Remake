from django.shortcuts import render
# from app.models import Subreddit, Post, Comment

# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, 'index_view.html', context)

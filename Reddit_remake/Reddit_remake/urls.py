"""Reddit_remake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from app.views import index_view, \
                      testing_view, \
                      CommentView, \
                      CommentCreateView, \
                      CommentDetailView, \
                      CommentUpdateView, \
                      PostView, \
                      PostCreateView, \
                      PostDetailView, \
                      SubredditView, \
                      SubredditDetailView, \
                      SubredditCreateView, \
                      SubredditUpdateView, \
                      UserCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', index_view, name="index_view"),
    url(r'^testing/', testing_view, name="testing_view"),

    #SUBREDDIT
    url(r'^subreddits/create$', SubredditCreateView.as_view(), name="subreddit_create_view"),
    url(r'^subreddits$', SubredditView.as_view(), name="subreddit_list_view"),
    url(r'^subreddits/(?P<pk>\d+)$', SubredditDetailView.as_view(), name="subreddit_detail_view"),
    url(r'^subreddits/(?P<pk>\d+)/update$', SubredditUpdateView.as_view(), name="subreddit_update_view"),
    # url(r'^post/create$', PostCreateView.as_view(), name="post_create_view"),

    #POSTS
    url(r'^subreddits/(?P<pk>\d+)/posts/create$', PostCreateView.as_view(), name="post_create_view"),
    url(r'^subreddits/(?P<pk>\d+)/posts/$', PostView.as_view(), name="post_list_view"),
    url(r'^posts/(?P<post_id>\d+)$', PostDetailView.as_view(), name="post_detail_view"),
    url(r'^posts/(?P<post_id>\d+)/update$', PostUpdateView.as_view(), name="post_update_view"),

    #COMMENTS
    url(r'^posts/(?P<post_id>\d+)/comments/create$', CommentCreateView.as_view(), name="comment_create_view"),
    url(r'^posts/(?P<post_id>\d+)/comments$', CommentView.as_view(), name="comment_list_view"),
    url(r'^comments/(?P<comment_id>\d+)$', CommentDetailView.as_view(), name="comment_detail_view"),
    url(r'^comments/(?P<comment_id>\d+)/update$', CommentUpdateView.as_view(), name="comment_update_view"),
    # url(r'^subreddits/(?P<pk>\d+)/post/(?P<post_id>\d+/comment/(?P<comment_id>\d+)/', CommentDeleteView.as_view(), name="comment_delete_view"),
]

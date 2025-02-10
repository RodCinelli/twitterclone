from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.tweets.models import Tweet
from apps.tweets.forms import TweetForm


@login_required
def home(request):
    tweets = Tweet.objects.select_related('user').prefetch_related('likes').all()
    form = TweetForm()
    return render(request, 'tweets/feed.html', {'tweets': tweets, 'form': form})

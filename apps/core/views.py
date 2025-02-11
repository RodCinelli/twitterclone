from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.tweets.models import Tweet
from apps.tweets.forms import TweetForm
from django.contrib.auth.models import User


@login_required
def home(request):
    tweets = Tweet.objects.select_related('user').prefetch_related('likes').all()
    form = TweetForm()
    return render(request, 'tweets/feed.html', {'tweets': tweets, 'form': form})

def search(request):
    query = request.GET.get('q', '')
    if query:
        tweets = Tweet.objects.filter(content__icontains=query)
        users = User.objects.filter(username__icontains=query)
    else:
        tweets = []
        users = []
    
    context = {
        'tweets': tweets,
        'users': users,
        'query': query,
    }
    
    if request.htmx:
        return render(request, 'partials/search_results.html', context)
    return render(request, 'search.html', context)

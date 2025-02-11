from django.urls import path
from .views import TweetCreateAPIView, toggle_like
from . import views

app_name = 'tweets'

urlpatterns = [
    path('create/', TweetCreateAPIView.as_view(), name='create_tweet'),
    path('like/<int:tweet_id>/', toggle_like, name='toggle_like'),
    path('auto-feed/', views.auto_feed, name='auto_feed'),
]

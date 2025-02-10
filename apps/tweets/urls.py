from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('create/', views.TweetCreateAPIView.as_view(), name='create_tweet'),
]

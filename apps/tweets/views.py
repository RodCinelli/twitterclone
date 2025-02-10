from rest_framework import generics
from django_htmx.http import trigger_client_event
from .models import Tweet
from .serializers import TweetSerializer


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetSerializer
    
    def get_success_headers(self, data):
        response = super().get_success_headers(data)
        if self.request.htmx:
            response = trigger_client_event(response, 'newTweet')
        return response

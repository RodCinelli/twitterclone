from rest_framework import generics
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import logging
from .models import Tweet
from .serializers import TweetSerializer

logger = logging.getLogger(__name__)

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            if request.htmx:
                tweet = get_object_or_404(Tweet, id=response.data['id'])
                html = render_to_string(
                    'tweets/partials/tweet_response.html',
                    {'tweet': tweet},
                    request=request
                )
                return HttpResponse(html)
            return response
        except Exception as e:
            logger.error(f"Error creating tweet: {str(e)}")
            return HttpResponse(
                "Erro ao criar tweet. Por favor, tente novamente.",
                status=500
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

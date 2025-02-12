from rest_framework import generics
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
import logging
from .models import Tweet
from .serializers import TweetSerializer
from .forms import TweetForm
from .utils.fake_data import (
    generate_random_tweet, 
    generate_tech_news_tweet, 
    ensure_fake_users_exist,
    get_fake_user,
    FAKE_USERS
)
import random
import json
from django.utils.timesince import timesince

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

def toggle_like(request, tweet_id):
    if not request.htmx:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    tweet = get_object_or_404(Tweet, id=tweet_id)
    user = request.user
    
    if tweet.likes.filter(id=user.id).exists():
        tweet.likes.remove(user)
        liked = False
    else:
        tweet.likes.add(user)
        liked = True
    
    like_count = tweet.likes.count()
    
    return JsonResponse({
        'liked': liked,
        'likeCount': like_count
    })

def get_random_tweet():
    """Retorna um tweet aleatório gerado."""
    if random.random() < 0.2:  # 20% de chance de ser uma notícia
        tweet_data = generate_tech_news_tweet()
    else:
        tweet_data = generate_random_tweet()
    
    return tweet_data

@login_required
def auto_feed(request):
    """View para o feed automático com tweets simulados."""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Garante que os usuários simulados existam
        ensure_fake_users_exist()
        
        # Gera um novo tweet
        tweet_data = get_random_tweet()
        
        # Obtém o usuário simulado do banco de dados
        fake_user = get_fake_user(tweet_data['user']['username'])
        
        # Cria o tweet com o usuário simulado
        new_tweet = Tweet.objects.create(
            content=tweet_data['content'],
            user=fake_user  # Usa o usuário simulado em vez do usuário logado
        )
        
        # Renderiza o tweet no formato correto
        html = render_to_string(
            'tweets/partials/tweet.html',
            {
                'tweet': new_tweet,
                'user': request.user,  # Usuário logado para verificar likes
                'fake_user': tweet_data['user']  # Dados de exibição do usuário simulado
            },
            request=request
        )
        
        return HttpResponse(html)
    
    return redirect('core:home')

@login_required
def search_tweets(request):
    """View para buscar tweets."""
    query = request.GET.get('q', '').strip()
    
    if query:
        # Obtém todos os tweets
        tweets = Tweet.objects.all().order_by('-created_at')
        
        # Filtra os tweets que correspondem à busca
        filtered_tweets = []
        for tweet in tweets:
            # Verifica se o tweet tem um usuário simulado associado
            fake_user = next((user for user in FAKE_USERS if user['username'] == tweet.user.username), None)
            
            # Adiciona o tweet se corresponder aos critérios de busca
            if (query.lower() in tweet.user.username.lower() or  # username real
                query.lower() in tweet.content.lower() or  # conteúdo do tweet
                (fake_user and (  # dados do usuário simulado
                    query.lower() in fake_user['username'].lower() or
                    query.lower() in fake_user['name'].lower()
                ))):
                filtered_tweets.append((tweet, fake_user))  # Guarda o tweet junto com seu fake_user
        
        tweets_with_users = filtered_tweets
    else:
        # Se não houver query, retorna todos os tweets com seus fake_users
        tweets = Tweet.objects.all().order_by('-created_at')
        tweets_with_users = [(tweet, next((user for user in FAKE_USERS if user['username'] == tweet.user.username), None)) 
                            for tweet in tweets]
    
    html = render_to_string(
        'tweets/partials/tweet_list.html',
        {
            'tweets_with_users': tweets_with_users,  # Passa a lista de tuplas (tweet, fake_user)
            'user': request.user
        },
        request=request
    )
    
    return HttpResponse(html)

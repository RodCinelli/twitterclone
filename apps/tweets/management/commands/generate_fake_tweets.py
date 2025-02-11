from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.tweets.models import Tweet
from apps.tweets.utils.fake_data import (
    generate_random_tweet,
    generate_tech_news_tweet,
    ensure_fake_users_exist,
    get_fake_user
)
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Gera tweets aleatórios para simular atividade no feed'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Número de tweets para gerar'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        # Garante que os usuários simulados existam
        ensure_fake_users_exist()
        self.stdout.write('Usuários simulados criados/verificados com sucesso')

        # Gera tweets aleatórios
        for _ in range(count):
            if random.random() < 0.2:  # 20% de chance de ser uma notícia
                tweet_data = generate_tech_news_tweet()
            else:
                tweet_data = generate_random_tweet()
            
            # Obtém o usuário simulado do banco de dados
            fake_user = get_fake_user(tweet_data['user']['username'])
            
            tweet = Tweet.objects.create(
                content=tweet_data['content'],
                user=fake_user  # Usa o usuário simulado em vez do admin
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Tweet criado com sucesso por @{fake_user.username}: {tweet.content[:50]}...'
                )
            ) 
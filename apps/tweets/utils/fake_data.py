import random
from django.contrib.auth import get_user_model

User = get_user_model()

FAKE_USERS = [
    {"username": "tech_guru", "name": "Tech Guru", "avatar": "👨‍💻"},
    {"username": "code_ninja", "name": "Code Ninja", "avatar": "🥷"},
    {"username": "python_lover", "name": "Python Lover", "avatar": "🐍"},
    {"username": "web_dev", "name": "Web Developer", "avatar": "👩‍💻"},
    {"username": "data_scientist", "name": "Data Scientist", "avatar": "📊"},
    {"username": "ai_expert", "name": "AI Expert", "avatar": "🤖"},
    {"username": "ux_designer", "name": "UX Designer", "avatar": "🎨"},
    {"username": "cloud_arch", "name": "Cloud Architect", "avatar": "☁️"},
    {"username": "security_pro", "name": "Security Pro", "avatar": "🔒"},
    {"username": "mobile_dev", "name": "Mobile Dev", "avatar": "📱"},
]

TWEET_TEMPLATES = [
    "Acabei de aprender sobre {tech}! 🚀",
    "Alguém mais está empolgado com {tech}? 😍",
    "Desenvolvendo um novo projeto com {tech} 💻",
    "O futuro da tecnologia está em {tech} 🔮",
    "{tech} é incrível! Não consigo parar de estudar 📚",
    "Dica do dia: comece a aprender {tech} 💡",
    "Quem mais está usando {tech} nos seus projetos? 🤔",
    "Tutorial de {tech} chegando em breve! 📝",
    "Impressionado com as possibilidades de {tech} ✨",
    "Resolvendo bugs em {tech} é minha paixão 🐛",
]

TECHNOLOGIES = [
    "Python", "Django", "JavaScript", "React", "Docker",
    "Kubernetes", "AWS", "Machine Learning", "Data Science",
    "Cloud Computing", "DevOps", "CI/CD", "Git", "APIs",
    "Microservices", "Node.js", "Vue.js", "Angular", "TypeScript",
    "GraphQL", "MongoDB", "PostgreSQL", "Redis", "Blockchain",
]

def generate_random_tweet():
    """Gera um tweet aleatório com um usuário aleatório."""
    user = random.choice(FAKE_USERS)
    template = random.choice(TWEET_TEMPLATES)
    tech = random.choice(TECHNOLOGIES)
    
    content = template.format(tech=tech)
    
    return {
        "user": user,
        "content": content,
    }

def generate_tech_news_tweet():
    """Gera um tweet de notícia tecnológica."""
    news_templates = [
        "🔥 Última hora: Nova versão de {tech} lançada!",
        "📢 Breaking: {tech} anuncia recursos revolucionários",
        "📱 Tendência: {tech} está transformando o mercado",
        "🚀 {tech} atinge marca histórica de usuários",
        "💡 Novidade: {tech} apresenta solução inovadora",
    ]
    
    template = random.choice(news_templates)
    tech = random.choice(TECHNOLOGIES)
    
    return {
        "user": {"username": "tech_news", "name": "Tech News", "avatar": "📰"},
        "content": template.format(tech=tech),
    }

def ensure_fake_users_exist():
    """Garante que todos os usuários simulados existam no banco de dados."""
    for fake_user in FAKE_USERS:
        user, created = User.objects.get_or_create(
            username=fake_user['username'],
            defaults={
                'email': f"{fake_user['username']}@example.com",
                'first_name': fake_user['name']
            }
        )
        if created:
            user.set_password('fake_user_123')
            user.save()
    
    # Garante que o usuário de notícias também existe
    news_user, created = User.objects.get_or_create(
        username='tech_news',
        defaults={
            'email': 'tech_news@example.com',
            'first_name': 'Tech News'
        }
    )
    if created:
        news_user.set_password('fake_user_123')
        news_user.save()

def get_fake_user(username):
    """Retorna um usuário simulado do banco de dados."""
    return User.objects.get(username=username) 
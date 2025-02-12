#!/bin/sh

echo "Aplicando as migrations..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Criando site no Django..."
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.get_or_create(id=1, defaults={'domain': 'twitterclone-production-1f3e.up.railway.app', 'name': 'TwitterClone'})"

echo "Iniciando a aplicação..."
exec "$@" 
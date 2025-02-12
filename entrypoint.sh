#!/bin/sh

postgres_ready() {
    nc -z $SQL_HOST $SQL_PORT
}

# Aguarda o PostgreSQL
until postgres_ready; do
    echo >&2 "PostgreSQL não está disponível - aguardando..."
    sleep 1
done
echo >&2 "PostgreSQL está disponível - continuando..."

echo "Aplicando as migrations..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Criando site no Django..."
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.get_or_create(id=1, defaults={'domain': 'localhost:8000', 'name': 'TwitterClone'})"

echo "Iniciando a aplicação..."
exec "$@" 
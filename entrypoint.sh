#!/bin/sh
# Aguarda o banco de dados ficar disponível (ajuste o tempo conforme necessário)
sleep 5

echo "Aplicando as migrations..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando a aplicação..."
exec "$@" 
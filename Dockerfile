# Utilizando versão mais recente do Python
FROM python:3.12-slim AS python-base

    # Configurações do Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Configurações do pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Nova versão do Poetry
    POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # Caminhos
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adicionando Poetry ao PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Instalando dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        gcc \
        python3-dev \
        netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install psycopg2-binary gunicorn requests

# Instalação do Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - --version ${POETRY_VERSION} \
    && chmod +x /opt/poetry/bin/poetry

# Copiar e instalar dependências do projeto
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Configurar Poetry para não criar ambiente virtual e instalar dependências
RUN /opt/poetry/bin/poetry config virtualenvs.create false \
    && /opt/poetry/bin/poetry install --no-root

# Configuração final do workspace
WORKDIR /app
COPY . /app/

# Copia o entrypoint e torna-o executável
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Define o entrypoint e o comando padrão
ENTRYPOINT ["/app/entrypoint.sh"]
CMD sh -c "gunicorn twitterclone.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2 --threads 4 --access-logfile - --error-logfile - --log-level info --capture-output"
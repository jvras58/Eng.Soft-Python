# Dockerfile
FROM python:3.11-slim AS base

# Instala as dependências do sistema e o uv (que gerencia o venv)
RUN pip install --no-cache-dir uv uvicorn

WORKDIR /app

# Copia o código para o container
COPY . .

# Cria o ambiente virtual com o uv
RUN uv venv

# Sincroniza as dependências no ambiente virtual
RUN . .venv/bin/activate && uv sync

# Define variável de ambiente padrão (pode ser sobrescrita no docker-compose)
ENV ENVIRONMENT=prod

# Copia o script de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Define o entrypoint
CMD ["/entrypoint.sh"]
